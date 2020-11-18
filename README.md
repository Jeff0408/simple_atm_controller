# Simple_atm_controller
This project can be cloned by entering: git clone https://github.com/Jeff0408/simple_atm_controller.git

## Program detail
This program is to simulate a simple atm.  
After running this py, the following flow is below  

Default card number : 123456789  
Default PIN number : 1234  
Default Cash in your wallet : 10000  
Default Balance in checking account : 1000  
Default Balance in savings account : 1000  
You can change these default values in py  

The flow :
#### 1.Insert Card (you should enter your card number)  
####   => 2.PIN number (you should enter PIN number)  
####     => 3.Select Account   
####       => 4.Leave/See Balance/Deposit/Withdraw  
This program will show your curret balance in your chosen account and current amount of cash in your wallet in step 4.  
If you have any typo, there will be a hint to let you enter command again, and you can do "See Balance", "Deposit" and "Withdraw" until you enter "Leave" until you enter "Leave".   
If you enter Leave in the last step, you will quit this program.  

## Running the Program

This program can be executed by simply running:  
python3 controller.py in the command line  
