## Preq & How to run the web app?

```
You have two choices:

1. Run it with docker. Therefore, you have to install docker. To run the app, navigate to the root directory which contains the file "docker-compose.yml". Then, run the following command "docker-compose up --build".

2. Run it with Makefile. Therefore, you need to install Node & Python 3 and you need to make sure that your enviroment support "Makefile". Then, run this command "`make -j2`". If this couldn't work, I would suggest you to navigate to each folders (backend and frontend) and read their Readmes. Moreover, this requires as well the following:
    - Navigate to the file index.vue, replace this line 'http://fast-api:8000/get_lists' with this 'http://localhost:8000/get_lists'
    - Navigate to the file __main__ in api folder, and add those lines after last import 
        HOST = os.environ.get('HOST', 'localhost')
        PORT = int(os.environ.get('PORT', 8000))
      and replace 'run()' with run(HOST, PORT)

```

## High Level Description

```
A checking tool for internal JSONs that store data. These JSONs are checked, everytime our checking system finds an error, it generates a JSON error object like:


{
    "index": SOME_NUMERIC_INDEX,
    "code": SOME_NUMERIC_ERROR_CODE,
    "text": SOME_TEXT_DESCRIPTION
}

An API that will get all errors generated so far, seperated by their status. A human operator has to be able to see and understand these errors in order to fix them in the original data. As a result, it will educe errors to almost zero by providing a flawless UI/UX for operators to check errors and resolve them.
```

## The Features

-  The available error categories: resolved, unresolved, backlog.

```
_frontend_

-   [x] A "nice" overview of all errors, it should show `unresolved`, then `resolved` and then `backlog` errors
-   [x] View the `text` and `code` of each error
-   [x] Resolve `unresolved` error(s) locally
-   [x] Unresolve each individual `resolved` error(s) locally 
-   [x] Move an individual backlog error to `unresolved` locally
-   [X] Shadows,
-   [X] Click, hover animations (e.g. changing to a darker shade of said color)
```

```
_backend_

-   [x] Retrieve error list (resolved, unresolved and backlog lists) api. Trace how many request received this api for a specific operator and logs how many request in total for this api. 

-   [x] Retrieve the intersection counts between (resolved & unresolved), (unresolved & backlog), and (resolved & backlog).
-   [x] Retrieve & logs how many requests for errors are received.
-   [x] Retrieve & logs how many requests for errors are received from a specific operator
-   [x] the operator can send all errors that are currently marked as `resolved` to the `api`, the `api` prints out how many times a certain `error.code` was resolved
```

## Screenshots

Some screenshots to give you a scence of the UI.

