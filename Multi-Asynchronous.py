import asyncio

async def monitor_cpu():
    await asyncio.sleep(1)
    return "CPU usage high"

async def monitor_network():
    await asyncio.sleep(2)
    return "Unusual traffic detected"

async def run_monitors():
    alerts = await asyncio.gather(monitor_cpu(), monitor_network())
    for alert in alerts:
        print(alert)

asyncio.run(run_monitors())
