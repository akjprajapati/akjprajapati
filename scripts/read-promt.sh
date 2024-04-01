#!/bin/bash
read -p "Please enter your age: " age 
if [[ "$age" =~ '^[0-9]+$' ]] 
   then 
        echo "Your age is $age."

   else
        echo "error: Not a number."
fi
