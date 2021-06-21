# uncompyle6 version 3.7.4
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.8.5 (default, Sep  3 2020, 21:29:08) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: ps2_verify_movement36.py
# Compiled at: 2017-03-22 00:32:29
# Size of source mod 2**32: 804 bytes


def testRobotMovement(robot_type, room_type, delay=0.4):
    """
    Runs a simulation of a single robot of type robot_type in a 5x5 room.
    """
    import ps2_visualize
    room = room_type(5, 5)
    robot = robot_type(room, 1)
    anim = ps2_visualize.RobotVisualization(1, 5, 5, delay)
    while room.getNumCleanedTiles() < room.getNumTiles():
        robot.updatePositionAndClean()
        anim.update(room, [robot])

    anim.done()