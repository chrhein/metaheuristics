import sys


def progress(i):
    if i >= 9999:

        sys.stdout.write("\033[F")

        print("Progress: Complete                                \n")
    elif i == 9750:
        sys.stdout.write("\033[F")
        print("Progress: ########################################")
    elif i == 9500:
        sys.stdout.write("\033[F")
        print("Progress: #######################################-")
    elif i == 9250:
        sys.stdout.write("\033[F")
        print("Progress: ######################################--")
    elif i == 9000:
        sys.stdout.write("\033[F")
        print("Progress: #####################################---")
    elif i == 8750:
        sys.stdout.write("\033[F")
        print("Progress: ####################################----")
    elif i == 8500:
        sys.stdout.write("\033[F")
        print("Progress: ###################################-----")
    elif i == 8250:
        sys.stdout.write("\033[F")
        print("Progress: ##################################------")
    elif i == 8000:
        sys.stdout.write("\033[F")
        print("Progress: #################################-------")
    elif i == 7750:
        sys.stdout.write("\033[F")
        print("Progress: ################################--------")
    elif i == 7500:
        sys.stdout.write("\033[F")
        print("Progress: ###############################---------")
    elif i == 7250:
        sys.stdout.write("\033[F")
        print("Progress: ##############################----------")
    elif i == 7000:
        sys.stdout.write("\033[F")
        print("Progress: #############################-----------")
    elif i == 6750:
        sys.stdout.write("\033[F")
        print("Progress: ############################------------")
    elif i == 6500:
        sys.stdout.write("\033[F")
        print("Progress: ###########################-------------")
    elif i == 6250:
        sys.stdout.write("\033[F")
        print("Progress: ##########################--------------")
    elif i == 6000:
        sys.stdout.write("\033[F")
        print("Progress: #########################---------------")
    elif i == 5750:
        sys.stdout.write("\033[F")
        print("Progress: ########################----------------")
    elif i == 5500:
        sys.stdout.write("\033[F")
        print("Progress: #######################-----------------")
    elif i == 5250:
        sys.stdout.write("\033[F")
        print("Progress: ######################------------------")
    elif i == 5000:
        sys.stdout.write("\033[F")
        print("Progress: #####################-------------------")
    elif i == 4750:
        sys.stdout.write("\033[F")
        print("Progress: ####################--------------------")
    elif i == 4500:
        sys.stdout.write("\033[F")
        print("Progress: ###################---------------------")
    elif i == 4250:
        sys.stdout.write("\033[F")
        print("Progress: ##################----------------------")
    elif i == 4000:
        sys.stdout.write("\033[F")
        print("Progress: #################-----------------------")
    elif i == 3750:
        sys.stdout.write("\033[F")
        print("Progress: ################------------------------")
    elif i == 3500:
        sys.stdout.write("\033[F")
        print("Progress: ###############-------------------------")
    elif i == 3250:
        sys.stdout.write("\033[F")
        print("Progress: ##############--------------------------")
    elif i == 3000:
        sys.stdout.write("\033[F")
        print("Progress: #############---------------------------")
    elif i == 2750:
        sys.stdout.write("\033[F")
        print("Progress: ############----------------------------")
    elif i == 2500:
        sys.stdout.write("\033[F")
        print("Progress: ###########-----------------------------")
    elif i == 2250:
        sys.stdout.write("\033[F")
        print("Progress: ##########------------------------------")
    elif i == 2000:
        sys.stdout.write("\033[F")
        print("Progress: #########-------------------------------")
    elif i == 1750:
        sys.stdout.write("\033[F")
        print("Progress: ########--------------------------------")
    elif i == 1500:
        sys.stdout.write("\033[F")
        print("Progress: #######---------------------------------")
    elif i == 1250:
        sys.stdout.write("\033[F")
        print("Progress: ######----------------------------------")
    elif i == 1000:
        sys.stdout.write("\033[F")
        print("Progress: #####-----------------------------------")
    elif i == 750:
        sys.stdout.write("\033[F")
        print("Progress: ####------------------------------------")
    elif i == 500:
        sys.stdout.write("\033[F")
        print("Progress: ###-------------------------------------")
    elif i == 250:
        sys.stdout.write("\033[F")
        print("Progress: ##--------------------------------------")
    elif i == 0:
        sys.stdout.write("\033[F")
        print("Progress: #---------------------------------------")
