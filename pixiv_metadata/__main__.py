import aiohttp
from loguru import logger
import re
import asyncio


api_url = "https://www.pixiv.net/ajax/illust/"
headers = {
    "Host": "www.pixiv.net",
    "referer": "https://www.pixiv.net/",
    "origin": "https://accounts.pixiv.net",
    "accept-language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
}


async def get_metadata(session: aiohttp.ClientSession, pid: str) -> dict:
    try:
        async with session.get(f"{api_url}{pid}", headers=headers) as response:
            ret = await response.json()
            if ret["error"]:
                raise Exception(
                    f"Error: Download Metadata Error when handling {pid}, message: {ret['message']}"
                )
            return ret["body"]
    except Exception as e:
        raise e


def extract_tags(meta: dict) -> list[str]:
    try:
        tag_list = meta["tags"]["tags"]
        ret = []
        for tag in tag_list:
            if "translation" in tag and "en" in tag["translation"]:
                ret.append(tag["translation"]["en"])
            else:
                ret.append(tag["tag"])
        return ret
    except Exception:
        return []


def get_extra_tags(meta: dict) -> list[str]:
    """Generate extra functional tags."""
    ret = []

    # Artist
    ret.append(f"Artist:{meta['userId']}")  # use userId to avoid name change

    # Bookmark
    if meta["bookmarkCount"] >= 10000:
        ret.append("BookmarkCount:10000+")
    elif meta["bookmarkCount"] >= 5000:
        ret.append("BookmarkCount:5000+")
    elif meta["bookmarkCount"] >= 1000:
        ret.append("BookmarkCount:1000+")

    return ret


def gen_note(meta: dict) -> str:
    desc = meta["description"].replace(r"<br />", "\n")
    return f"""Title:{meta["title"]}
Id:{meta["id"]}
BookmarkCount:{meta["bookmarkCount"]}
Artist:{meta["userName"]}
ArtistId:{meta["userId"]}
Description:
{desc}"""


# Modify Here
# I use the format `name12345.jpg` or `name12345_p1.jpg` as my filename
# the more popular format is `12345.jpg` or `12345_p1.jpg`
# if so, use the commented regex
# reg = re.compile(r"([0-9]+)(_p[0-9]+)?\.(jpg|png|gif|webp)")
reg = re.compile(
    r"(([A-Za-z0-9]+?)|([A-Za-z]*[0-9]+_))([0-9]+)(_p[0-9]+)?\.(jpg|png|gif|webp)"
)


def get_pid(filename: str) -> str | None:
    match = reg.match(filename)
    if match is None:
        return None
    try:
        # Modify Here
        # if you have modified the regex, then uncomment the next line
        # return match.group(1)
        return match.group(4)
    except Exception:
        return None


# Modify Here
# Change it to your eagle api url, usually http://127.0.0.1:41595
# but may vary if you are running eagle on another machine
# or running this script in WSL2
EAGLE_API_URL = "http://127.0.0.1:41595"


async def get_target_list(session: aiohttp.ClientSession):
    # Modify Here
    # I use folder to filter what pictures I will handle
    # You can just delete the "folders": ... param
    # or change it to your own folder
    # or use any other filter options if you like.
    try:
        res = await session.get(
            EAGLE_API_URL + "/api/item/list",
            params={"limit": "9999", "folders": "LB6HFOM1W8YG9"},
        )
        res = await res.json()
        return res["data"]
    except Exception as e:
        logger.exception(
            f"Error when trying to get target id list from eagle. Exception:{e}"
        )


async def update_target(
    session: aiohttp.ClientSession, id: str, tags: list[str], annotation: str, url: str
):
    try:
        res = await (
            await session.post(
                EAGLE_API_URL + "/api/item/update",
                json={
                    "id": id,
                    "tags": tags,
                    "annotation": annotation,
                    "url": url,
                },
            )
        ).json()
        if res["status"] != "success":
            logger.error(
                f"Failed to update Eagle target {id}, tags {tags}, annotation {annotation}, url {url}, ret:{res}"
            )
        elif res["status"] == "success":
            logger.info(f"Successfully updated Eagle target {id}, Pixiv Picture {url}")
    except Exception as e:
        logger.exception(
            f"Exception when upading Eagle target {id}, tags {tags}, annotation {annotation}, url {url}, Exception:{e}"
        )


async def fetch_target(session: aiohttp.ClientSession, obj: dict):
    try:
        name = obj["name"]
        # Note that the name is not the filename, but without suffix. Append a suffix here to maintain compatibility
        name = name + ".jpg"
        pid = get_pid(name)
        if pid is None:
            logger.error(f"Error when handling obj {obj}, skipping.")
            return
        meta = await get_metadata(session, pid)
        ori_tags = obj["tags"]
        tags = extract_tags(meta)
        extra_tags = get_extra_tags(meta)

        final_tags = set()
        final_tags.update(ori_tags)
        final_tags.update(tags)
        final_tags.update(extra_tags)

        anno = gen_note(meta)
        url = f"https://www.pixiv.net/en/artworks/{pid}"

        await update_target(session, obj["id"], list(final_tags), anno, url)

    except Exception as e:
        logger.exception(f"Exception when handling obj {obj}, skipping. Exception:{e}")


async def main():
    session = aiohttp.ClientSession()
    targets = await get_target_list(session)
    if targets is None:
        logger.error("Failed to get target list.")
    else:
        await asyncio.gather(*[fetch_target(session, x) for x in targets])
    await session.close()


if __name__ == "__main__":
    # Modify Here
    # comment this to disable logging to file, which may be very redundant
    logger.add(
        "log.txt",
        rotation="1 MB",
        backtrace=True,
        diagnose=True,
        encoding="utf-8",
        enqueue=True,
    )

    asyncio.run(main())
