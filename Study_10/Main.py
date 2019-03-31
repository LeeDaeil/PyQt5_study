from collections import deque
from multiprocessing import Manager
from Study_10.CNS_UDP import *
from Study_10.CNS_Fun import *
# from .CNS_GFun import * # 인터페이스 설계로 인한 제외
from Study_10.CNS_CFun import *


class body:
    def __init__(self):
        #==== Initial part for testing===========================================================#
        self.a3c_test_mode = True
        self.shut_up = True
        #========================================================================================#
        self.shared_mem = generate_mem().make_mem_structure()
        self.UDP_net = [UDPSocket(self.shared_mem, IP='', Port=7001, shut_up=self.shut_up)]

        if self.a3c_test_mode:
            self.process_list = [
                clean_mem(self.shared_mem, shut_up=self.shut_up),
                interface_function(self.shared_mem),
                Autonomous_system(self.shared_mem),

                # function1(self.shared_mem),
                # function2(self.shared_mem),
                # function3(self.shared_mem),
                # gfunction(self.shared_mem), # 인터페이스 설계로 인한 제외
                # gfunction2(self.shared_mem), # 인터페이스 설계로 인한 제외
            ]
        else:
            self.process_list = [
                clean_mem(self.shared_mem, shut_up=self.shut_up),

            ]

    def start(self):
        print('A3C test mode : {}'.format(self.a3c_test_mode))
        job_list = []
        for __ in self.UDP_net:
            __.start()
            job_list.append(__)
        time.sleep(1)
        for __ in self.process_list:
            __.start()
            job_list.append(__)
        for job in job_list:
            job.join()

class generate_mem:
    def make_autonomous_mem(self):
        memory_dict = {'Man_state': False, 'Auto_state': True, 'Man_require': False,
                       'Current_op': 'LSTM-based algorithm', #'['LSTM-based algorithm', 'Tech Spec action', 'Ruel-based algorithm'],
                       'Strategy_out': ['[00:00:00] Start - Normal Operation - LSTM-base algorithm',
                                        '[00:00:46] Emergency Operation - LSTM-base algorithm'],
                       'Auto_operation_out': ['[00:00:00] Start',
                                              '[00:00:46] Reactor Trip',
                                              '[00:00:57] SI Valve Open',
                                              '[00:00:58] Charging Pump 1 Start',
                                              '[00:00:58] Aux Feed Water Pump 1 Start',
                                              '[00:00:58] Aux Feed Water Pump 3 Start',
                                              '[00:00:59] Aux Feed Water Control Valve (HV313) Open',
                                              '[00:00:59] Aux Feed Water Control Valve (HV315) Open',
                                              '[00:01:25] Aux Feed Water Pump 2 Start',
                                              '[00:01:27] Aux Feed Water Control Valve (HV314) Open',
                                              '[00:02:06] MSIV Close (HV108, HV208, HV308',
                                              '[00:04:36] RCP 1 Stop',
                                              '[00:04:36] RCP 2 Stop',
                                              '[00:04:36] RCP 3 Stop',
                                              ]}
        return memory_dict

    def make_test_mem(self):
        memory_dict = {'Test': 0, 'List_Test': []}
        return memory_dict

    def make_test_list_mem(self):
        memory_list = []
        return memory_list

    def make_CNS_time_mem(self):
        memory_list = []
        return memory_list

    def make_clean_mem(self):
        memory_dict = {'Clean': True}
        return memory_dict

    def make_main_mem_structure(self, max_len_deque=10, show_main_mem=False):
        memory_dict = {}
        with open('./db.txt', 'r') as f:
            while True:
                temp_ = f.readline().split('\t')
                if temp_[0] == '':  # if empty space -> break
                    break
                sig = 0 if temp_[1] == 'INTEGER' else 1
                memory_dict[temp_[0]] = {'V': 0, 'L': [], 'D': deque(maxlen=max_len_deque), "type": sig}
                # memory_dict[temp_[0]] = {'V': 0, 'L': [], 'D': deque(maxlen=max_len_deque), "type": sig,
                #                          'N_V': 0, 'N_L': [], 'N_D': deque(maxlen=max_len_deque)}  # Noise parameter
        if show_main_mem:
            print(memory_dict)
        return memory_dict

    def make_mem_structure(self, show_mem_list=False):
        memory_list = [Manager().dict(self.make_main_mem_structure(max_len_deque=10)),  # [0]
                       Manager().dict(self.make_test_mem()),
                       Manager().list(self.make_test_list_mem()),
                       Manager().dict(self.make_autonomous_mem()),                      # [-3]
                       Manager().list(self.make_CNS_time_mem()),                        # [-2]
                       Manager().dict(self.make_clean_mem()),                           # [-1]
                       ]
        '''
        개인이 설계한 메모리를 추가로 집어 넣을 것.
        ex) 
            memory_list = [Manager().dict(self.make_main_mem_structure(max_len_deque=10)),
                           Manager().dict(자신이 설계한 메모리 구조)),
                           ...
                           Manager().dict(self.make_clean_mem()),]
        '''
        if show_mem_list:
            i = 0
            for __ in memory_list:
                print('{}번째 리스트|{}'.format(i, __))
                i += 1
        return memory_list


if __name__ == '__main__':
    main_process = body()
    main_process.start()