import uasyncio as asyncio
from machine import Pin


step = Pin(21, Pin.OUT)
dir = Pin(20, Pin.OUT)
step2 = Pin(10, Pin.OUT)
dir2 = Pin(11, Pin.OUT)
led = Pin(25, Pin.OUT)


async def adelante():
    dir.value(0)
    dir2.value(1)
    while True:
        step.value(1)
        step2.value(1)
        led.value(1)
        await asyncio.sleep(0.001)
        step.value(0)
        step2.value(0)
        led.value(0)
        await asyncio.sleep(0.001)

async def atras():
    dir.value(1)
    dir2.value(0)
    while True:
        step.value(1)
        step2.value(1)
        led.value(1)
        await asyncio.sleep(0.001)
        step.value(0)
        step2.value(0)
        led.value(0)
        await asyncio.sleep(0.001)

async def derecha():
    dir.value(0)
    dir2.value(0)
    while True:
        step.value(1)
        step2.value(1)
        led.value(1)
        await asyncio.sleep(0.001)
        step.value(0)
        step2.value(0)
        led.value(0)
        await asyncio.sleep(0.001)

async def izquierda():
    dir.value(1)
    dir2.value(1)
    while True:
        step.value(1)
        step2.value(1)
        led.value(1)
        await asyncio.sleep(0.001)
        step.value(0)
        step2.value(0)
        led.value(0)
        await asyncio.sleep(0.001)

async def stop():
    step.value(0)
    step2.value(0)
    led.value(0)


async def command_handler():
    while True:
        command = input("Instruccion: ").strip().lower()

        if command == "adelante":
            asyncio.create_task(adelante())
        elif command == "atras":
            asyncio.create_task(atras())
        elif command == "derecha":
            asyncio.create_task(derecha())
        elif command == "izquierda":
            asyncio.create_task(izquierda())
        elif command == "stop":
            await stop()
        else:
            print("Invalid command")

        await asyncio.sleep(0)


async def main():
    await command_handler()


asyncio.run(main())
