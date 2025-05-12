REQUIREMENTS
 streamlit
scikit-learn
numpy
pandas
Homebrew - check this youtube for installation of " homebrew " - https://www.youtube.com/watch?v=flQxyoyBX5M
libomp - pip3 install libomp






How to run ?
How to install streamlit ?
" pip3 install streamlit "
now run "streamlit run app.py"

If above command fails then run the following commands
   ( to check the streamlit installation path)-If this returns nothing, it means the streamlit executable isn't linked to your shell's PATH properly.
     "which streamlit" 
   
   You can run Streamlit by using its full path. First, find the location of the Streamlit executable with the following: 
     "find /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages -name "streamlit" "
       
       Once you locate the full path to the executable, you can run it directly like this:
       " python3 -m streamlit run app.py "


       NOTE : Or if you are sure the executable exists, use the full path like this:
              " /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/streamlit/bin/streamlit run app.py  "


In order to run the flask application like app.py , first we have to create a virtual environment using the command in terminal " python3 -m venv venv "
Now activate the environment variable using this command " source venv/bin/activate "

Now run this command  " pip install flask "
Now run your " app.py " in terminal 


   