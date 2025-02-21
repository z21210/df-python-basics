# Making and Testing HTTP Requests

## Aims

The aims of this session is to introduce the idea of making HTTP requests and interacting with APIs.  We will also look at how to test code that makes HTTP requests.

---

## Learner Stories

```text
As a DATA PROFESSIONAL,  
I want to be able to make HTTP REQUESTS and INTERACT with APIs,  
so that I can COLLECT DATA from WEB SERVICES and INTEGRATE them into my DATA PIPELINE
```

---

## Definition of DONE

- [ ] The data professional has completed a tutorial or training session on making HTTP requests and interacting with APIs in Python, focusing on libraries such as requests.
- [ ] The data professional can explain the purpose of making HTTP requests, common methods (GET, POST, PUT, DELETE), and how APIs are used to retrieve or send data.

The data professional has written scripts demonstrating:

- [ ] Making basic HTTP GET requests to retrieve data from an API endpoint.
- [ ] Handling different HTTP methods (e.g., POST requests to send data).
- [ ] Parsing JSON or XML responses from APIs.
- [ ] Handling HTTP response status codes and errors.

The data professional has completed exercises that demonstrate:

- [ ] Authenticating requests using API keys or OAuth.
- [ ] Sending parameters and headers in requests.
- [ ] Handling paginated responses from APIs.
- [ ] Integrating API responses into a data pipeline or processing workflow.

- [ ] Code reviews have been conducted for these scripts, confirming that API interactions are correctly implemented and follow best practices.
- [ ] The data professional has created a script that demonstrates the end-to-end process of making HTTP requests, handling responses, and integrating data into a pipeline or application.
- [ ] All scripts are formatted according to PEP 8 guidelines and adhere to Python best practices.
- [ ] All scripts have been successfully executed in a Jupyter Notebook environment, with correct API interactions and expected results.
- [ ] The data professional has completed a quiz or assessment on HTTP requests and API interactions and passed with a score of at least 80%.
- [ ] Examples of API interactions are documented in a shared knowledge repository or personal learning journal.
- [ ] Feedback from peers or mentors on API interactions has been reviewed, and any suggested improvements have been implemented.

---

## HTTP Requests and Responses

These are the back-bone of any transfer of information across the Internet.  We make a request for information and the endpoint we are requesting from sends a response.  This can take many forms, from a simple web page to a complex API response.

![HTTP Request/Response Cycle](../images/HTTPRequests.png)

### HTTP Request Structure

HTTP Requests have:

- Request Line
- Zero or more header fields followed by CRLF \(\\r\\n\)
- An empty line \(CRLF\) indicating the end of the header fields
- An optional message body \(ie\.\, data / content\)

```
POST /php/myapplication.php HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5; Windows NT)
Host: www.example.com
Content-Type: application/x-www-form-urlencoded
Content-Length: length
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Connection: Keep-Alive

key=value&username=example&email=me@example.com
```

### HTTP Response Structure

HTTP Responses have:

- a status line
- Zero or more header fields followed by CRLF \(\\r\\n\)
- An empty line \(\\r\\n\)
- An optional message body\(data\, content\)

```
HTTP/1.1 200 OK
Date: Mon, 21 Mar 2016 09:15:56 GMT
Server: Apache/2.2.14 (Win32)
Last-Modified: Mon, 21 Mar 2016 09:14:01 GMT
Content-Length: 88
Content-Type: text/html
Connection: Closed

<html>
<body>
<h1>Hello, World!</h1>
</body>
</html>
```

### HTTP Verbs

Most Common:

- __GET__ \-\- Retrieve information for a given URI
- __POST__ \-\- Send data to the given URI
- __PUT__ \-\- Replace data at the given URI
- __DELETE__ \-\- Remove data at the given URI

Rarely used:

- HEAD
- OPTIONS
- TRACE

#### Example GET Request

```
GET /index.php HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5; Windows NT)
Host: www.example.com
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Connection: Keep-Alive
```

#### Example DELETE Request

```
DELETE /users/id/1012 HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5; Windows NT)
Host: www.example.com
```

### GET Requests

GET requests have no request body

- The URI specifies most of the data the server requires:
  - The protocol, eg. `HTTP`
  - The host, eg. `example.com`
  - The resource location, eg. `/index.php`
  - The query string, eg. `?username=eg&email=foo@example.com`
  - The query string contains associative key/value pairs
    - Technically limited to 255 characters however in practice they can be over 1000 long
- Other information can be supplied with headers, either standard ones or custom headers typically preceded by `X-`

### POST Requests

- POST requests _build on_ GET requests by including a message body
  - They can use the query string system _and_ the message body to send data
  - Larger or more sensitive information is usually sent via POST
    - The message body can have a practically unlimited size \(usually limited by what the server will accept\,eg\. 20MB\)
    - The browser sends the POST body "behind the scenes" whereas the URL is visible in the address bar
- POST messages are _not_ more secure than GET messages however
  - Both are sent "plain text" over the network
- Use HTTPS for encryption

### HTTP Status Codes

| Status Code Pattern | Pattern Family | Example | Example Meaning       | Example Information                        |
| ------------------- | -------------- | ------- | --------------------- | ------------------------------------------ |
| 1\*\*               | Informational  | 102     | Processing            | Processing still going on                  |
| 2\*\*               | Successful     | 201     | Created               |                                            |
| 3\*\*               | Redirection    | 301     | Moved Permanently     | Resource has moved to a different location |
| 4\*\*               | Client Errors  | 404     | Not Found             | The requested resource could not be found  |
| 5\*\*               | Server Errors  | 500     | Internal Server Error | A problem with the responding server       |

> Quick Quiz Question: What is the meaning of status code 418?

### HTTP Headers

- Headers are key-value pairs
- They are used to send additional information about the request or response between the client and the server

These are used to help verify the integrity of the request/response and that the data is being sent/received correctly.

#### Common Request Headers

- `User-Agent` - The user agent string of the client
- `Host` - The host name of the server
- `Accept` - The MIME types the client can accept
- `Content-Type` - The MIME type of the request body
  - `application/x-www-form-urlencoded` - Form data
  - `application/json` - JSON data
  - `text/plain` - Plain text

#### Common Response Headers

- `Date` - The date and time the response was sent
- `Server` - The server software
- `Content-Length` - The length of the response body
- `Content-Type` - The MIME type of the response body
  - `application/json` - JSON data
  - `text/html` - HTML data

For example, if you are sending JSON data to a server, you would set the `Content-Type` header to `application/json`.  If you then sent HTML to the server, the server can be set to reject the request before it processes anything as it was expecting JSON data.

The same can work in reverse, if the server sends back JSON data and the client is expecting HTML, the client can reject the response.

---

## Making HTTP Requests in Python

### The `requests` Library

The `requests` library is a popular library for making HTTP requests in Python.  It is a third-party library and is not included in the Python standard library.

To install the `requests` library, use the following command:

```bash
pip install requests
```

You can see the [documentation for the `requests` library here](https://docs.python-requests.org/en/master/).

### Making a GET Request

To make a GET request using the `requests` library, use the `requests.get()` function.  This function returns a [`Response`](https://docs.python-requests.org/en/latest/api/#requests.Response) object.

```python
import requests

response = requests.get('https://api.github.com')
print(response.text)                                # .text is one of the properties - what else is there?
```

### Checking a Response

The `Response` object has a number of properties that can be used to check the response:

- `status_code` - The status code of the response
- `headers` - The headers of the response
- `text` - The content of the response, in text format

```python
import requests

response = requests.get('https://api.github.com')

print(f'Status Code: {response.status_code}')

if response.status_code == 200:
    print('Success!')
else:
    print('An error occurred.')
```

To gracefully handle non-200 status codes, applications should still return a response to the user, even if it is an error message.  You may wish to log the error for auditing and debugging purposes.

`raise_for_status()` is a method that can be called on the `Response` object to raise an exception if the response is not successful.

```python
import requests

response = requests.get('https://madeupnotreturningurl.com')

response.raise_for_status()
```

---

### Testing Code that Makes HTTP Requests

When testing code that makes HTTP requests, it is important to consider the following:

- The code should be tested with both successful and unsuccessful responses
- The code should be tested with different status codes
- The code should be tested with different response content
- The code should be tested with different headers (if they are used    )
- The code should be tested with different request methods (if they are used)
- The code should be tested with different request bodies (if they are used)

If we are writing a unit test, we do not want to make the actual request to the server.  Instead, we can use a ___mock___ to simulate the response.

#### Use the `unittest.mock` module to `patch` the function to be called and specify the return values

This actually creates a mock dictionary that we can use to specify the values of any properties that we want to return.

```python
from unittest.mock import patch
import requests

def get_request(url):
    response = requests.get(url)
    return response.text

def test_get_request():
    # Arrange
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '<html><p>Hello, World!</p></html>'

        # Act
        response = get_request('https://www.github.com')

        # Assert
        assert response.text == '<html><p>Hello, World!</p></html>'
```

This code will not actually make a call to the server, instead, when the function being tested calls `requests.get()`, it will return the response specified in the test.

> The whole world would come crashing down if GitHub returned "Hello, World!" in an HTML response!

---

### Testing for Exceptions

Testing becomes more efficient if you are able to use the same code to test for different Exceptions.

`pytest` allows you to use a concept called decorators to specify the expected exception. `pytest.mark.parameterize` allows you to pass in a list of exceptions and the error messages that they carry.  In the test, where `exception` is used will pass in the first exception in the list and where `error_message` is used will pass in the first error message in the list.  The test will then rerun with the second exception and error message and so on.

```python
import pytest
from requests.exceptions import Timeout, RequestException

@pytest.mark.parametrize("exception, error_message", [
    (
        Exception("An error occurred"),
        "An error occurred - Unexpected error for URL"
    ),
    (
        Timeout("The request timed out"),
        "The request timed out - Request failed for URL"
    ),
    (
        RequestException("Invalid URL"),
        "Invalid URL - Request failed for URL"
    )
])
```

This code provides a number of exceptions that can be passed to a test function.  The test function can then be written to check for the different exceptions and the error messages they carry.

```python
def test_get_request_handles_exceptions(exception, error_message):
    # Arrange
    with patch('requests.get') as mock_get:
        mock_get.side_effect = exception

        # Act
        with pytest.raises(RequestException) as exc_info:
            response = get_request('https://www.github.com')

        # Assert
        assert str(exc_info.value) == error_message
```

`mock_get.side_effect = exception` is used to specify the exception that should be raised when the function is called.  `with pytest.raises(RequestException) as exc_info:` is used to check that the exception is raised and to capture the exception information.

---
