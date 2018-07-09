from ..exceptions.tardisexceptions import AsyncRunCommandFailure

import asyncio


async def async_run_command(cmd, *args):
    sub_process = await asyncio.create_subprocess_exec(cmd, *args, stdout=asyncio.subprocess.PIPE,
                                                       stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await sub_process.communicate()

    if not sub_process.returncode:
        return stdout.decode().strip()

    raise AsyncRunCommandFailure(message=stdout, error_code=sub_process.returncode, error_message=stderr)