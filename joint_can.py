import can
import math


class JointData():
    position=0
    speed=0
    torque=0
    bearing_temp=0
    FSM=0
    MC_error=0
    MC_error_occured=0
    joint_error=0
    joint_warning=0
    MA_val=0
    motor_temp=0
    
def send_msg(adr, data, bus):
    msg = can.Message(arbitration_id=adr, data=data, is_fd=False, is_extended_id=False)
    try:
        bus.send(msg,1)
        # print(f"Message sent on {bus.channel_info}")
    except can.CanError:
        print("Message NOT sent")
        
    return bus.recv(1)

def get_data(rcv_msg,bus):
    data=rcv_msg.data
    if len(data)<16:
        return JointData()
    joint_data=JointData()
    joint_data.position=float(int.from_bytes(data[0:4],'big',signed=True))*math.pi/2147483647
    joint_data.speed=float(int.from_bytes(data[4:6],'big',signed=True))*2/32767
    joint_data.torque=float(int.from_bytes(data[6:8],'big',signed=True))*360/32767
    joint_data.bearing_temp=data[8]
    joint_data.FSM=data[9]
    joint_data.MC_error=data[10]
    joint_data.MC_error_occured=data[11]
    joint_data.joint_error=data[12]
    joint_data.joint_warning=data[13]
    joint_data.MA_val=int.from_bytes(data[14:16],'big',signed=True)
    joint_data.motor_temp=data[16]

    return joint_data

def set_speed(speed,bus):
    speed_data=(int)(speed*32767/2)
    speed_data=speed_data.to_bytes(2,'big',signed=True)
    return get_data(send_msg(0x000,speed_data,bus),bus)

def set_torque(torque,bus):
    torque_data=(int)(torque*32767/360)
    torque_data=torque_data.to_bytes(2,'big',signed=True)
    return get_data(send_msg(0x000,torque_data,bus),bus)