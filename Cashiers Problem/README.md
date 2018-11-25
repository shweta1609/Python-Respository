The goal of this challenge is to design a cash register program. <br/>You will be given two decimal numbers. The first is the purchase price (PP) of the item. The second is the cash (CH) given by the customer. Your register currently has the following bills/coins within it: 
<br/>
'PENNY': .01,<br/>
'NICKEL': .05,<br/>
'DIME': .10,<br/>
'QUARTER': .25,<br/>
'HALF DOLLAR': .50,<br/>
'ONE': 1.00,<br/>
'TWO': 2.00,<br/>
'FIVE': 5.00,<br/>
'TEN': 10.00,<br/>
'TWENTY': 20.00,<br/>
'FIFTY': 50.00,<br/>
'ONE HUNDRED': 100.00<br/>
The aim of the program is to calculate the change that has to be returned to the customer.
<br/><br/>Input:<br/>
Your program should read lines of text from standard input. Each line contains two numbers which are separated by a semicolon. The first is the Purchase price (PP) and the second is the cash(CH) given by the customer.
<br/>Output:<br/>
For each line of input print a single line to standard output which is the change to be returned to the customer. In case the CH < PP, print out ERROR. If CH == PP, print out ZERO. For all other cases print the amount that needs to be returned, in terms of the currency values provided. The output should be alphabetically sorted.