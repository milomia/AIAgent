# Introduction
	This is a simple demo of what a small python program can do. It uses a local llm and has
one dependency key but allows a user to put a pdf into the data directory where he/she can query 
the pdf. The example provided is just my CV but it could be anything.

## Dependencies
	To get this to work you will need to add a key to a .env file 
which contains LLAMA_CLOUD_API_KEY the key is from the website
https://cloud.llamaindex.ai/project/6889925f-982f-4ee8-880c-cdcd382253b7/extraction
and is free to add

It also requires a local install of ollama which can be dowloaded from 
git@github.com:ollama/ollama.git it uses the mistral model which can be got by
running ollama: run mistral - this is a 4GB download so will take a while. There 
are a lot larger models available but require significant hardware to run.

## Running 
	The program can be run by installing the requirements.txt into a suitable 
virtual environment and running python main.py
example running session:

(mike projects-py3.11) michaelhunt@MacBookPro AIAgent % python main.py
Started parsing the file under job_id 1317f1b1-c71d-4b54-84fc-831cb5f6f559
Enter a prompt (q to quit): when did michael hunt leave olive jar
 Michael Hunt left Olive Jar in August 2024.
Enter a prompt (q to quit): what languages does michael know
 Michael is proficient in several programming languages including Python, R, VBA, C#, Java, C++, JavaScript, MATLAB, Ruby, Bash/dos, as well as various libraries and frameworks for each language.
Enter a prompt (q to quit): q
(mike projects-py3.11) michaelh
