import json, os
import aiofiles


async def read_from_json(filename: str) -> list:
    try:
        async with aiofiles.open(filename, "r", encoding="utf-8") as r_json:
            data = await r_json.read()
            # print(data)
            return json.loads(data)
    except FileNotFoundError:
        await write_in_json(filename, [])
        return []
    except Exception as e:
        print(f"read_from_json --- Ошибка: {e}")
        return []


async def write_in_json(filename: str, data):
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        if not os.path.exists(filename):
            async with aiofiles.open(filename, "w", encoding="utf-8") as f:
                await f.write("[]") 

        async with aiofiles.open(filename, "w", encoding="utf-8") as w_json:
            await w_json.write(json.dumps(data, ensure_ascii=False, indent=4))
    except Exception as e:
        print(f"write_in_json --- Ошибка: {e}")


async def delete_chat_from_json(filename: str, key: str, value: str):
    try:
        from_json = await read_from_json(filename=filename)
        for index, item in enumerate(from_json):
            if item[f"{key}"] == value:
                del from_json[index]
            else:
                pass

        await write_in_json(filename=filename, data=from_json)
    except Exception as e:
        print(f"delete_from_json --- Ошибка: {e}")


async def add_to_json(filename: str, data: dict):
    try:
        if os.path.getsize(filename) != 0:
            from_file_data = await read_from_json(filename)
            if data not in from_file_data:
                from_file_data.append(data)
            
            await write_in_json(filename, from_file_data)
        else:
            await write_in_json(filename, data)
    except Exception as e:
        print(f"Ошибка: {e}")     