# HPDF-Assignment-1-Python-Flask

Following tasks was assigned to be completed by week 1 :

                                                Backend : Python-Flask 
 
1) A simple hello-world at http://localhost:8080/ that displays a simple string like 
                                  "Hello World - Nikhil" (replace "Nikhil" with your own first name). 
 
2) Add a route, for e.g. http://localhost:8080/authors, which: 
                      a) fetches a list of authors from a request to https://jsonplaceholder.typicode.com/users 
                      b) fetches a list of posts from a request to https://jsonplaceholder.typicode.com/posts 
                      c) Respond with only a list of authors and the count of their posts (a newline for each author). 

3) Set a simple cookie (if it has not already been set) at http://localhost:8080/setcookie with the following values: 
                                  name=<your-first-name> and age=<your-age>. 
 
4) Fetch the set cookie with http://localhost:8080/getcookies and display the stored key-values in it. 
 
5) Deny requests to your http://localhost:8080/robots.txt page. 
(or you can use the response at http://httpbin.org/deny if needed) 
 
6) Render an HTML page at http://localhost:8080/html or an image at http://localhost:8080/image.
 
7) A text box at http://localhost:8080/input which sends the data as POST to any endpoint of your choice. This endpoint should log the received the received to stdout. 

                                  SOLUTION TO THE ABOVE PROBLEM STATEMENTS AND DEMO TO RUN THE PROJECT

To run the project :
1. Clone the repository to your local system.
2. Make sure all the dependancies(Python, Flask) have been installed on your system.
3. Go to the root folder of the project where app.py is located. Right click anywhere in the window and open terminal at that location.
4. Type the following command in the terminal window :
                                                            python app.py
5. After running the server, check the localhost address and the port number on which project is deployed.
6. Open any web browser, paste the localhost address along with port number.
7. Open any of the end point mentioned in the problem section above to check project.
