#!/usr/bin/env python3


"""
Caveat when attempting to run the examples in non-gps environments:

`drone.offboard.stop()` will return a `COMMAND_DENIED` result because it
requires a mode switch to HOLD, something that is currently not supported in a
non-gps environment.
"""


import asyncio


from mavsdk import System
from mavsdk.offboard import (OffboardError, PositionGlobalYaw)




async def run():
    """ Does Offboard control using position NED coordinates. """


    drone = System()
    await drone.connect(system_address="udp://:14540")


    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break


    print("Waiting for drone to have a global position estimate...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- Global position estimate OK")
            break


    print("-- Arming")
    await drone.action.arm()


    print("-- Setting initial setpoint")
    await drone.offboard.set_position_global(PositionGlobalYaw(47.39775284421333, 8.545618586840646, 488.9983658625417, 0.0, 1))


    print("-- Starting offboard")
    try:
        await drone.offboard.start()
    except OffboardError as error:
        print(f"Starting offboard mode failed with error code: {error._result.result}")
        print("-- Disarming")
        await drone.action.disarm()
        return


    print("-- Go 0m North, 0m East, -5m Down within local coordinate system")
    await drone.offboard.set_position_global(PositionGlobalYaw(47.39775284421333, 8.545618586840646, 50.0, 0.0))
    await asyncio.sleep(10)


    print("-- Go 5m North, 0m East, -5m Down within local coordinate system, turn to face East")
    await drone.offboard.set_position_global(PositionGlobalYaw(47.39796163210049, 8.545553451121236, 50.0, 0.0))
    await asyncio.sleep(10)


    print("-- Go 5m North, 10m East, -5m Down within local coordinate system")
    await drone.offboard.set_position_global(PositionGlobalYaw(47.39791981835066, 8.545844880837365, 50.0, 0.0))
    await asyncio.sleep(10)


    print("-- Go 0m North, 10m East, 0m Down within local coordinate system, turn to face South")
    await drone.offboard.set_position_global(PositionGlobalYaw(47.39771612, 8.54592565, 50.0, 0.0))
    await asyncio.sleep(10)

    print("-- Go 0m North, 10m East, 0m Down within local coordinate system, turn to face South")
    await drone.offboard.set_position_global(PositionGlobalYaw(47.39757138523519, 8.545684905636023, 50.0, 0.0))
    await asyncio.sleep(10)

    print("-- Go 0m North, 10m East, 0m Down within local coordinate system, turn to face South")
    await drone.offboard.set_position_global(PositionGlobalYaw(47.39761962838268, 8.545398230450246, 50.0, 0.0))
    await asyncio.sleep(10)

    print("-- Go 0m North, 10m East, 0m Down within local coordinate system, turn to face South")
    await drone.offboard.set_position_global(PositionGlobalYaw(47.397826546339175, 8.545326965636605, 50.0, 0.0))
    await asyncio.sleep(10)

    print("-- Go 0m North, 10m East, 0m Down within local coordinate system, turn to face South")
    await drone.offboard.set_position_global(PositionGlobalYaw(47.39796056, 8.54555503, 50.0, 0.0))
    await asyncio.sleep(10)

    print("-- Stopping offboard")
    try:
        await drone.offboard.stop()
    except OffboardError as error:
        print(f"Stopping offboard mode failed with error code: {error._result.result}")




if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
