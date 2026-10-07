"""Local question bank and evaluation for mock interviews."""

from __future__ import annotations

import random
from typing import Any

LETTERS = ("A", "B", "C", "D")


def _question(prompt: str, options: tuple[str, str, str, str], answer: int, explanation: str) -> dict[str, Any]:
    return {
        "question": prompt,
        "options": list(options),
        "answer": options[answer],
        "explanation": explanation,
    }


QUESTION_BANK: dict[str, dict[str, list[dict[str, Any]]]] = {
    "Full Stack Development": {
        "Beginner": [
            _question("What does HTML primarily describe?", ("The structure of a web page", "The database schema", "The server operating system", "The network route"), 0, "HTML elements describe the structure and meaning of page content."),
            _question("Which language is used to style web pages?", ("CSS", "SQL", "Bash", "XML"), 0, "CSS controls the presentation and layout of HTML content."),
            _question("What does JavaScript commonly add to a web page?", ("Interactive behavior", "Disk partitioning", "Database backups", "Email delivery"), 0, "JavaScript can respond to events and update page content in the browser."),
            _question("Which HTML element is most appropriate for a page's main heading?", ("<h1>", "<span>", "<footer>", "<meta>"), 0, "The h1 element identifies the primary heading of a page or section."),
            _question("What is the DOM?", ("A tree representation of a document that scripts can inspect and change", "A type of CSS selector only", "A database query language", "A web hosting plan"), 0, "The Document Object Model represents page nodes as an object tree."),
            _question("What is the main role of a web server in a basic web application?", ("Receive requests and send responses", "Render every monitor pixel", "Compile CSS into SQL", "Assign keyboard shortcuts"), 0, "A web server handles HTTP requests and returns resources or application responses."),
            _question("Which format is commonly used to exchange structured data between web services?", ("JSON", "JPEG", "MP3", "BMP"), 0, "JSON represents structured data in a widely supported text format."),
            _question("What does responsive web design aim to do?", ("Adapt a layout to different screen sizes", "Make a site work only offline", "Replace HTML with images", "Prevent all user input"), 0, "Responsive layouts adjust to available screen space and device characteristics."),
            _question("What is Git commonly used for?", ("Tracking changes to source code", "Encrypting all network traffic", "Serving HTML pages", "Designing database tables"), 0, "Git records source changes and supports collaboration through version control."),
            _question("In a browser, what does an HTTP link usually identify?", ("A resource that can be requested", "A local variable", "A CSS color", "A CPU instruction"), 0, "A URL identifies a resource and the protocol used to request it."),
            _question("Which HTML element creates a link to another resource?", ("<a>", "<table>", "<strong>", "<section>"), 0, "The anchor element uses its href attribute to link to a URL or page location."),
            _question("What is a frontend in a web application?", ("The parts users interact with in a browser", "Only the database server", "The physical network cable", "A source-control branch"), 0, "The frontend is the user-facing application, usually rendered in the browser."),
        ],
        "Intermediate": [
            _question("Which HTTP method is generally intended to retrieve a resource without changing it?", ("GET", "POST", "PATCH", "DELETE"), 0, "GET is defined as a safe method for retrieving a representation."),
            _question("What does a database index primarily improve?", ("The speed of certain lookups", "The correctness of every write", "The size of every response", "The number of application users"), 0, "Indexes can reduce the amount of data a database scans for supported queries."),
            _question("Why should a web application validate input on the server?", ("Client-side checks can be bypassed", "Browsers never send strings", "It removes the need for authorization", "It prevents all network failures"), 0, "A client is under user control, so the server must enforce its own input rules."),
            _question("What problem does a CSRF token help prevent?", ("A browser being tricked into making an unwanted authenticated request", "A slow database query", "A missing CSS file", "A malformed image"), 0, "An unpredictable token can demonstrate that a state-changing request came from the application flow."),
            _question("What does a 404 HTTP status indicate?", ("The requested resource was not found", "The request succeeded with content", "The client must authenticate", "The server has permanently moved"), 0, "HTTP 404 means the server did not find a current representation for the target resource."),
            _question("Why are parameterized SQL queries preferred?", ("They separate SQL code from user-supplied values", "They automatically encrypt the database", "They make every query faster", "They disable database constraints"), 0, "Bound parameters keep input data from being interpreted as executable SQL syntax."),
            _question("What does CORS control in browsers?", ("Which cross-origin responses browser scripts may access", "Which database tables exist", "How HTML headings are sized", "How passwords are hashed"), 0, "Cross-Origin Resource Sharing is a browser-enforced policy for cross-origin requests."),
            _question("What is the purpose of a database transaction?", ("Group operations so they satisfy defined all-or-nothing behavior", "Convert HTML into JavaScript", "Cache every page permanently", "Replace authentication"), 0, "Transactions provide atomicity and other guarantees for related database operations."),
            _question("What does a reverse proxy commonly do?", ("Forward client requests to one or more backend services", "Replace a relational database", "Run code inside the browser DOM", "Define a programming language"), 0, "A reverse proxy sits in front of backend services and can route or manage incoming requests."),
            _question("Why should an application avoid storing a plaintext password?", ("A data breach would reveal the original passwords", "Plaintext cannot be sent over HTTP", "It prevents users from signing in", "It makes salts impossible"), 0, "A strong password-hashing scheme limits damage if stored credentials are exposed."),
            _question("What does a cache-control max-age directive specify?", ("How long a response may be considered fresh", "The maximum database row count", "The number of HTTP headers", "The password expiration date"), 0, "max-age gives a freshness lifetime for a cached response."),
            _question("What does an API version help a service manage?", ("Compatibility as its interface evolves", "The speed of the user's keyboard", "A browser's font rendering", "The number of database backups"), 0, "Versioning can let clients migrate while a service changes its contract."),
        ],
        "Expert": [
            _question("In a browser event loop, when are promise callbacks typically run?", ("As microtasks after the current JavaScript stack completes", "Before the current function begins", "Only after a full page reload", "On a separate process by definition"), 0, "Promise reactions are queued as microtasks and run after the current stack unwinds."),
            _question("What is a common purpose of optimistic concurrency control?", ("Detect conflicting updates without locking every read", "Encrypt a database backup", "Guarantee that no requests fail", "Avoid validating user input"), 0, "Optimistic concurrency checks a version or condition at write time and rejects stale updates."),
            _question("What does snapshot isolation generally provide to a transaction?", ("A consistent snapshot of data for its reads", "A guarantee against every possible write skew", "A global lock on all database users", "An automatic schema migration"), 0, "Snapshot isolation gives a transaction a stable view, though it does not prevent every anomaly."),
            _question("Why can cache invalidation be difficult in a distributed application?", ("Copies may become stale across nodes and invalidation can race with writes", "Caches cannot store strings", "HTTP has no status codes", "Databases cannot update rows"), 0, "Distributed copies and concurrent updates make consistent invalidation a coordination problem."),
            _question("What does hydration mean in server-rendered web applications?", ("Attaching client-side behavior to server-rendered markup", "Encrypting HTML before storage", "Converting a database to JSON", "Compressing CSS into an image"), 0, "Hydration initializes client-side code around markup already rendered on the server."),
            _question("What is eventual consistency?", ("Replicas may temporarily differ but converge if updates stop", "Every read always sees the latest global write", "A transaction cannot be retried", "A cache never expires"), 0, "Eventual consistency permits temporary divergence with convergence under suitable conditions."),
            _question("In a blue-green deployment, what is the green environment typically used for?", ("The new version that can receive traffic after validation", "A permanently isolated database backup", "A user's local browser cache", "The source-code formatter"), 0, "Blue-green deployments keep parallel environments and switch traffic after the new one is ready."),
            _question("What is the main risk of retrying a non-idempotent operation after a timeout?", ("The operation may be applied more than once", "The server must change its hostname", "The request becomes a GET", "The response is guaranteed to be cached"), 0, "A timeout does not reveal whether the server completed the operation, so blind retry may duplicate effects."),
            _question("What is a useful property of a correlation ID in distributed tracing?", ("It links related work across service boundaries", "It authenticates a user by itself", "It encrypts the transport", "It guarantees transaction isolation"), 0, "A propagated correlation ID helps operators connect logs and traces from one request."),
            _question("Why might a circuit breaker stop sending requests to a failing dependency?", ("To limit cascading failures and allow recovery", "To increase the dependency's database size", "To bypass all authorization", "To force every request to succeed"), 0, "A circuit breaker fails fast during sustained faults and periodically permits recovery checks."),
            _question("What is the key trade-off when choosing a very long cache lifetime for mutable data?", ("Better cache reuse but potentially staler responses", "Fewer database indexes but more tables", "More secure passwords but slower hashing", "Smaller HTML but larger source code"), 0, "Longer freshness lifetimes reduce origin requests while delaying visibility of updates."),
            _question("What does the N+1 query problem describe?", ("One query loads a list and an additional query runs for each item", "A query returns exactly N plus one rows", "A database has one more index than table", "An HTTP request retries once"), 0, "N+1 behavior creates repeated per-record database calls and can cause excessive latency."),
        ],
    },
    "Java": {
        "Beginner": [
            _question("What is the JVM responsible for?", ("Executing Java bytecode", "Styling web pages", "Designing relational schemas", "Translating DNS names"), 0, "The Java Virtual Machine executes compiled Java bytecode."),
            _question("Which method is the conventional entry point of a Java application?", ("public static void main(String[] args)", "start(String value)", "run(int count)", "init()"), 0, "The launcher looks for a compatible public static main method."),
            _question("Which Java type stores a whole number primitive?", ("int", "boolean", "char[]", "StringBuilder"), 0, "int is Java's primitive type for 32-bit signed integer values."),
            _question("Which statement creates a String variable named name?", ("String name = \"Ada\";", "text name = \"Ada\";", "string name := \"Ada\";", "char name = \"Ada\";"), 0, "String is the Java class used for immutable sequences of characters."),
            _question("Which keyword declares a class in Java?", ("class", "struct", "define", "moduleclass"), 0, "The class keyword declares a class type."),
            _question("What does an if statement do?", ("Runs a block when a condition is true", "Repeats a block a fixed number of times", "Imports a package", "Creates a new thread"), 0, "An if statement selects a block based on a boolean condition."),
            _question("Which loop is commonly used to visit each item in an array?", ("for", "package", "throws", "import"), 0, "A for loop can iterate through array indexes or use the enhanced for form."),
            _question("What is an object in Java?", ("An instance of a class", "A source-code comment", "A compiler warning", "A package name"), 0, "A class defines a type; an object is a runtime instance of that type."),
            _question("Which value represents a boolean false value?", ("false", "0.0", "\"false\"", "null"), 0, "false is one of the two boolean literals in Java."),
            _question("What does an array's length field provide?", ("The number of elements in the array", "The last valid index", "The size of each object in bytes", "The array's element type"), 0, "For an array named values, values.length is its element count."),
            _question("Which keyword can make a variable unassignable after initialization?", ("final", "static", "public", "native"), 0, "A final variable can be assigned only once."),
            _question("What is a Java package commonly used for?", ("Organizing related types and avoiding name conflicts", "Running a database query", "Encrypting a network connection", "Creating a loop"), 0, "Packages organize types into namespaces and support access organization."),
        ],
        "Intermediate": [
            _question("Why should equals and hashCode be consistent for objects used as HashMap keys?", ("Equal keys must have the same hash code for correct bucket lookup", "Both methods must return strings", "HashMap calls only equals", "The methods control garbage collection"), 0, "Hash-based collections use hashCode to find candidates and equals to confirm equality."),
            _question("What does a Java generic type provide?", ("Compile-time type parameterization", "Automatic database persistence", "Runtime source-code compilation for every call", "A replacement for classes"), 0, "Generics let APIs express relationships between types and catch many mismatches at compile time."),
            _question("What is a checked exception?", ("An exception the compiler requires code to catch or declare", "An exception that cannot be thrown", "A syntax error", "A subclass of every runtime exception"), 0, "Checked exceptions must be handled or included in a method's throws declaration."),
            _question("What does try-with-resources do?", ("Closes declared AutoCloseable resources automatically", "Retries a failed method forever", "Catches every exception silently", "Starts a background thread"), 0, "Resources declared in try-with-resources are closed when the statement exits."),
            _question("What does Stream.map typically do?", ("Transform each stream element into another value", "Remove all duplicate elements", "Sort a collection in place", "Close the JVM"), 0, "map applies a function to each element and produces a stream of mapped values."),
            _question("What does the synchronized keyword help provide?", ("Mutual exclusion and memory visibility around a monitor", "Automatic immutability", "A database transaction", "Compile-time generic specialization"), 0, "A synchronized block acquires a monitor and establishes visibility guarantees on release and acquire."),
            _question("What is the difference between == and equals for many Java objects?", ("== compares references; equals can compare logical value", "== compares strings by value in all cases", "equals compares object addresses only", "There is no difference"), 0, "Unless overridden, equals may also compare identity, but many classes implement value equality."),
            _question("What is a functional interface?", ("An interface with one abstract method", "An interface with no methods", "A class with only static fields", "An interface that cannot use generics"), 0, "A functional interface has one abstract method and can be implemented with a lambda."),
            _question("What does Optional<T> represent?", ("A value that may or may not be present", "A thread-safe mutable list", "A checked exception", "A database connection pool"), 0, "Optional makes the possible absence of a return value explicit in an API."),
            _question("What does volatile guarantee for a Java field?", ("Visibility of writes across threads, not atomicity of compound updates", "Atomic increment for every expression", "Mutual exclusion for all methods", "Persistence after process exit"), 0, "volatile establishes visibility and ordering guarantees but does not make read-modify-write atomic."),
            _question("What is method overriding?", ("A subclass provides an implementation of an inherited instance method", "A method calls itself", "A class declares two constructors", "A package imports another package"), 0, "Overriding lets a subtype provide behavior for a method declared by a supertype."),
            _question("What does a Java record primarily provide?", ("A concise declaration for data-carrier classes", "A persistent database table", "A background executor", "A mutable global variable"), 0, "Records generate common data-oriented members from their declared components."),
        ],
        "Expert": [
            _question("What does the Java Memory Model's happens-before relation establish?", ("Visibility and ordering guarantees between actions", "The exact CPU instruction count", "A guarantee that code never blocks", "A database commit order"), 0, "Happens-before is the formal relation used to reason about inter-thread visibility and ordering."),
            _question("What is type erasure in Java generics?", ("Generic type parameters are mostly removed from runtime type representations", "All objects are converted to strings", "The compiler deletes method bodies", "A class loses its superclass"), 0, "Type erasure preserves backward compatibility by compiling most generic type information away."),
            _question("What is the role of a class loader?", ("Load class definitions into the JVM", "Schedule database transactions", "Render HTML elements", "Hash user passwords"), 0, "Class loaders locate and define classes, often using parent delegation."),
            _question("Why can a HashMap lookup degrade when many keys share one hash bucket?", ("The map must examine more colliding entries", "The JVM disables garbage collection", "Keys become immutable", "The map converts values to files"), 0, "Collisions require additional equality checks; tree bins mitigate some heavy-collision cases in modern JDKs."),
            _question("What is a key property of a sealed Java class?", ("It restricts which types may extend or implement it", "It cannot have methods", "It is always immutable", "It cannot be compiled to bytecode"), 0, "A sealed type explicitly controls its permitted direct subtypes."),
            _question("What is a common benefit of CompletableFuture composition?", ("Chaining asynchronous stages without manually blocking between each one", "Making all operations transactional", "Guaranteeing tasks run on a new thread", "Removing exceptions from asynchronous code"), 0, "Completion stages allow asynchronous results to be transformed and composed."),
            _question("What is a common limitation of a stop-the-world garbage-collection pause?", ("Application threads are paused while the collector performs certain work", "The heap is permanently deleted", "All objects become strongly reachable", "The JVM stops compiling classes forever"), 0, "Some collection phases pause application threads, affecting latency."),
            _question("In Java 21, what are virtual threads designed to make more scalable?", ("Large numbers of mostly-blocking concurrent tasks", "GPU shader compilation", "Database schema migrations", "Primitive arithmetic"), 0, "Virtual threads are lightweight threads intended to simplify high-concurrency blocking workloads."),
            _question("What does the Java Memory Model say about a data race?", ("Conflicting accesses without a happens-before ordering can have unintuitive results", "It is always detected at compile time", "It only occurs in single-threaded code", "It automatically makes fields volatile"), 0, "Unsynchronized conflicting accesses are not safely ordered and can expose stale or inconsistent state."),
            _question("What is the purpose of the ForkJoinPool work-stealing approach?", ("Idle workers can take tasks from busy workers' queues", "Workers wait for a global lock before each task", "Tasks are sent to a remote database", "Every task runs in a separate process"), 0, "Work stealing balances fine-grained tasks by letting idle workers take available work."),
            _question("Why can final fields help with safe publication of immutable objects?", ("The memory model gives special initialization-safety guarantees to properly constructed final fields", "They make every referenced object deeply immutable", "They prevent all exceptions", "They force values to be stored on disk"), 0, "Final-field semantics support visibility of correctly initialized values after construction."),
            _question("What does a Java module's exports declaration control?", ("Which packages it makes accessible to other modules", "Which classes the garbage collector can see", "Which threads may use the CPU", "Which exceptions can be thrown"), 0, "A module exports selected packages as part of its accessible API."),
        ],
    },
    "Python": {
        "Beginner": [
            _question("What is Python?", ("A high-level programming language", "An operating system", "A database engine", "A web browser"), 0, "Python is a general-purpose programming language with a high-level syntax."),
            _question("Which syntax starts a comment in ordinary Python code?", ("#", "//", "<!--", "**"), 0, "A hash mark begins a comment that continues to the end of the line."),
            _question("Which built-in type stores an ordered, mutable collection?", ("list", "tuple", "bool", "NoneType"), 0, "Lists preserve order and support item updates and resizing."),
            _question("How do you define a function in Python?", ("def", "func", "function", "method"), 0, "The def keyword begins a function definition."),
            _question("What value represents the absence of a value in Python?", ("None", "null", "undefined", "void"), 0, "None is Python's singleton value representing no value."),
            _question("Which brackets create a dictionary literal?", ("{}", "[]", "()", "<>"), 0, "A dictionary literal uses braces containing key-value pairs."),
            _question("How does Python mark the body of an if statement?", ("Indentation", "Curly braces", "A begin keyword", "A colon after every statement"), 0, "Indentation defines suites of statements in Python."),
            _question("What does len(items) return for a list?", ("The number of items", "The last item", "The list's memory address", "The item type"), 0, "len returns the number of elements in a list."),
            _question("Which keyword begins a loop over each value in a collection?", ("for", "repeat", "foreach", "iterate"), 0, "Python uses for item in iterable to visit values."),
            _question("Which value is the Boolean true literal in Python?", ("True", "true", "1", "YES"), 0, "Python Boolean literals are capitalized as True and False."),
            _question("What does print(\"Hello\") do?", ("Writes Hello to the standard output stream", "Creates a file named Hello", "Defines a function", "Imports a module"), 0, "print displays its arguments using the current output stream by default."),
            _question("Which expression accesses the first item of a list named colors?", ("colors[0]", "colors[1]", "colors.first", "colors(-1)"), 0, "Python sequences use zero-based indexing, so index 0 is the first element."),
        ],
        "Intermediate": [
            _question("Why are mutable default arguments often a bug in Python functions?", ("The same default object is reused across calls", "Defaults are evaluated after every return", "Lists cannot be function arguments", "Python copies every default deeply"), 0, "Default expressions are evaluated once when the function is defined."),
            _question("What does a list comprehension create?", ("A new list from an iterable and an expression", "A generator that is always lazy", "A class definition", "A file handle"), 0, "A list comprehension evaluates an expression for selected items and builds a list."),
            _question("What does yield do inside a generator function?", ("Produce a value while preserving the function's suspended state", "Exit the Python process", "Define a class attribute", "Catch an exception"), 0, "yield returns a value to the caller and allows iteration to resume later."),
            _question("What is the purpose of a context manager used with with?", ("Manage setup and cleanup around a block", "Compile Python to SQL", "Declare a global variable", "Make every exception disappear"), 0, "Context managers coordinate entry and cleanup, such as closing a file."),
            _question("When should is generally be used instead of ==?", ("To test object identity, such as checking whether a value is None", "To compare strings by their contents", "To compare every list element", "To perform numeric addition"), 0, "is checks whether two references identify the same object; == checks equality."),
            _question("What is a decorator commonly used for?", ("Wrap or transform a function or class", "Create a database index", "Declare a loop", "Convert a tuple into a module"), 0, "A decorator takes a callable and returns a callable, often adding reusable behavior."),
            _question("What does *args collect in a function definition?", ("Extra positional arguments as a tuple", "Extra keyword arguments as a dictionary", "All local variables", "The function's return value"), 0, "The *args parameter gathers excess positional arguments into a tuple."),
            _question("What does **kwargs collect in a function definition?", ("Extra keyword arguments as a dictionary", "Extra positional arguments as a list", "Imported modules", "All exceptions raised"), 0, "The **kwargs parameter gathers excess keyword arguments into a dictionary."),
            _question("What is a shallow copy of a nested list?", ("A new outer container that may share nested objects", "A recursively independent copy of every object", "A reference to a serialized file", "A tuple with no shared values"), 0, "A shallow copy duplicates the outer container but retains references to contained objects."),
            _question("What does enumerate(items) provide during iteration?", ("An index and each corresponding item", "Only the final item", "A sorted copy", "A dictionary of methods"), 0, "enumerate yields pairs containing a counter and the corresponding value."),
            _question("What is the purpose of __init__ in a Python class?", ("Initialize a newly created instance", "Destroy the Python interpreter", "Import the class module", "Compare two modules"), 0, "__init__ initializes instance state after an instance has been created."),
            _question("What does a set help provide?", ("A collection of distinct hashable values", "An ordered sequence allowing duplicates by index", "A key-value mapping", "A file stream"), 0, "Sets store unique hashable elements and support efficient membership tests."),
        ],
        "Expert": [
            _question("In a standard GIL-enabled CPython build, what does the GIL primarily limit?", ("Simultaneous execution of Python bytecode by multiple threads in one process", "The number of files a process can open", "The number of installed packages", "The size of every Python integer"), 0, "The GIL serializes Python bytecode execution in standard builds, though I/O and native code can release it."),
            _question("What is a descriptor in Python?", ("An object implementing attribute access methods such as __get__ or __set__", "A type of generator expression", "A package lock file", "A syntax for a context manager"), 0, "Descriptors customize attribute access and underpin properties and many method behaviors."),
            _question("What does Python's method resolution order determine?", ("The order in which base classes are searched for attributes and methods", "The order files are saved to disk", "The order list items are garbage-collected", "The order keyword arguments are parsed"), 0, "The MRO defines deterministic lookup through a class hierarchy, including multiple inheritance."),
            _question("What is a key property of asyncio tasks?", ("They cooperatively schedule coroutine execution on an event loop", "Each task always owns a separate operating-system process", "They make blocking calls nonblocking automatically", "They run without any await points"), 0, "Asyncio tasks schedule coroutines cooperatively; blocking code can still block the event loop."),
            _question("What does a frozen dataclass prevent by default?", ("Rebinding its declared fields after initialization", "Reading its fields", "Creating instances", "Using type annotations"), 0, "A frozen dataclass blocks normal field assignment, but referenced mutable values can still mutate."),
            _question("Why can reference counting alone fail to reclaim a group of cyclic objects?", ("Objects in a cycle can keep one another's reference counts above zero", "Reference counts are only used for integers", "Cycles cannot contain Python objects", "The interpreter never tracks references"), 0, "Cyclic garbage collection supplements reference counting to detect unreachable cycles."),
            _question("What is the effect of defining __slots__ on a class?", ("It can restrict per-instance attributes and reduce instance overhead", "It makes instances automatically thread-safe", "It replaces the class constructor", "It serializes each instance to JSON"), 0, "Slots define permitted instance attributes and can avoid a per-instance dictionary."),
            _question("What does structural subtyping in Python typing emphasize?", ("Whether an object provides the required operations, rather than its declared base class", "Whether two objects have identical memory addresses", "Whether a class uses inheritance only", "Whether a function has a docstring"), 0, "Protocols support static structural typing based on compatible members."),
            _question("What does functools.lru_cache require of typical function arguments?", ("They must be hashable so calls can be used as cache keys", "They must all be strings", "They must be immutable classes", "They must be keyword-only"), 0, "The cache uses arguments as keys, so arguments must be hashable."),
            _question("Why can importing a module with side effects make software harder to test?", ("Importing may unexpectedly perform work before a test can control it", "Python modules cannot be mocked", "Imports always run in a separate process", "The module becomes immutable"), 0, "Import-time I/O or global mutation creates hidden dependencies and makes tests less isolated."),
            _question("What is the primary purpose of a weak reference?", ("Refer to an object without keeping it alive solely because of that reference", "Copy an object recursively", "Prevent all object mutation", "Lock an object between threads"), 0, "Weak references do not increase an object's strong reference count."),
            _question("What is the difference between a coroutine object and a scheduled asyncio Task?", ("A Task wraps and schedules a coroutine on the event loop", "A coroutine always runs in a process; a Task runs in a thread", "A Task cannot be awaited", "They are unrelated to asynchronous execution"), 0, "Creating a coroutine does not run it; a Task schedules that coroutine for execution."),
        ],
    },
    "Cyber Security": {
        "Beginner": [
            _question("What does confidentiality mean in the CIA security triad?", ("Information is accessible only to authorized parties", "Systems are always online", "Data is always correct", "Backups are never tested"), 0, "Confidentiality protects information from unauthorized disclosure."),
            _question("What is phishing?", ("A deceptive attempt to trick people into revealing information or taking unsafe actions", "A secure backup method", "A kind of encryption key", "A software update process"), 0, "Phishing uses deceptive messages or sites to steal information or induce harmful actions."),
            _question("What does multi-factor authentication add?", ("A second factor beyond a password", "A longer username", "An automatic backup", "An extra browser tab"), 0, "MFA requires evidence from multiple factor categories, making a stolen password less sufficient."),
            _question("What does HTTPS help protect while a browser communicates with a website?", ("Data in transit through encryption and server authentication", "A computer from every malware infection", "The accuracy of every web page", "A lost local file"), 0, "HTTPS uses TLS to protect transport confidentiality and integrity and authenticate the server."),
            _question("What is the principle of least privilege?", ("Give each account only the access needed for its tasks", "Give every user administrator access", "Share one account across a team", "Disable all account logging"), 0, "Least privilege limits permissions to what is necessary for a role or operation."),
            _question("What is malware?", ("Software designed to harm, exploit, or perform unauthorized actions", "Any encrypted file", "A legitimate security update", "A type of network cable"), 0, "Malware is malicious software such as ransomware, spyware, or a trojan."),
            _question("What does a cryptographic hash normally produce?", ("A fixed-length digest of input data", "A reversible copy of the original file", "A private network connection", "A user password reset"), 0, "A cryptographic hash maps arbitrary input to a fixed-size digest and is designed to be one-way."),
            _question("Why should software security updates be installed promptly?", ("They may fix known vulnerabilities", "They guarantee no future attacks", "They remove the need for backups", "They encrypt every stored file"), 0, "Updates often include patches for weaknesses attackers could otherwise exploit."),
            _question("What does a firewall commonly do?", ("Allow or block network traffic according to rules", "Create strong passwords for users", "Repair corrupted source code", "Store encrypted backups"), 0, "A firewall filters network traffic based on configured policy."),
            _question("Why are backups useful against ransomware?", ("They may allow recovery of data without relying on the attacker", "They prevent every phishing email", "They make all files public", "They replace software updates"), 0, "Known-good offline or protected backups can support recovery after data is encrypted or destroyed."),
            _question("Which is the safest response to an unexpected attachment asking you to enable macros?", ("Verify the sender and purpose through a trusted channel before opening it", "Enable macros immediately", "Forward it to everyone", "Disable antivirus first"), 0, "Unexpected attachments can deliver malware, so verify them before interacting."),
            _question("What does authentication establish?", ("The identity of a user or system", "The user's permissions for every resource", "Whether a website is popular", "How much disk space is available"), 0, "Authentication verifies an asserted identity; authorization determines permitted actions."),
        ],
        "Intermediate": [
            _question("How do parameterized SQL queries reduce injection risk?", ("They keep supplied values separate from SQL syntax", "They encrypt the database file automatically", "They remove the need for access control", "They block every network attack"), 0, "Binding values as data prevents them from changing the structure of the SQL statement."),
            _question("What is a common defense against reflected cross-site scripting?", ("Context-aware output encoding", "Storing passwords with Base64", "Disabling database indexes", "Using longer URLs"), 0, "Encoding untrusted output for its HTML or script context prevents it from becoming executable markup."),
            _question("How does a synchronizer CSRF token help protect a state-changing request?", ("The server checks an unpredictable token tied to the user's session", "It encrypts the database password", "It disables browser cookies", "It scans the user's computer for malware"), 0, "A same-session token is difficult for an attacking site to guess or read."),
            _question("Why should passwords be stored with a salted password-hashing algorithm?", ("It slows guessing and prevents identical passwords from having identical stored hashes", "It lets the server recover the original password", "It makes passwords shorter", "It removes the need for TLS"), 0, "A unique salt and slow password hash make offline cracking more costly and precomputed tables less useful."),
            _question("What does role-based access control assign permissions through?", ("Roles associated with user responsibilities", "Random URL paths", "Browser color themes", "Password length alone"), 0, "RBAC groups permissions into roles that can be assigned to users."),
            _question("What is the purpose of a SIEM system?", ("Collect and correlate security events to support monitoring and investigation", "Compile source code", "Replace all endpoint protections", "Generate TLS certificates automatically"), 0, "A SIEM centralizes logs and helps identify patterns that may indicate security incidents."),
            _question("What is network segmentation used for?", ("Limit unnecessary communication and contain lateral movement", "Make every device publicly reachable", "Remove the need for authentication", "Increase password reuse"), 0, "Segmentation separates systems so a compromise in one area is less likely to spread."),
            _question("What does DNS spoofing attempt to do?", ("Cause a name lookup to return a misleading address", "Encrypt every DNS response with a user password", "Patch a web server", "Create an email signature"), 0, "DNS spoofing manipulates name-resolution data to direct users to an unintended destination."),
            _question("What is the main purpose of an incident response plan?", ("Coordinate preparation, containment, investigation, recovery, and communication", "Guarantee incidents never occur", "Replace all security monitoring", "Automatically pay ransom demands"), 0, "A plan assigns responsibilities and steps for handling security events effectively."),
            _question("What does a digital certificate help a TLS client verify?", ("A server's identity and its public-key binding", "That the server has no software bugs", "That every page is truthful", "That a password is unique"), 0, "A certificate binds an identity to a public key and is validated through a trust chain."),
            _question("What is a secure way to handle an application secret?", ("Store it in a protected secret manager and restrict access", "Commit it in source code", "Send it in a URL query string", "Reuse it across unrelated systems"), 0, "Secret stores support controlled access, rotation, and reduced accidental exposure."),
            _question("What does an endpoint detection and response tool help with?", ("Detecting and investigating suspicious activity on endpoints", "Replacing secure software development", "Making every user an administrator", "Encrypting DNS names"), 0, "EDR collects endpoint activity and supports detection, investigation, and response."),
        ],
        "Expert": [
            _question("What is a server-side request forgery (SSRF) vulnerability?", ("An attacker causes a server to make requests to unintended destinations", "A user submits too many valid passwords", "A browser loads a large image", "A database index is missing"), 0, "SSRF abuses a server's network position to reach internal or otherwise restricted resources."),
            _question("What is a core idea of zero-trust security?", ("Continuously verify access rather than trusting a network location by default", "Trust every request from inside the office", "Disable identity checks after login", "Use one shared administrator account"), 0, "Zero trust bases access on explicit identity, device, and context checks rather than implicit perimeter trust."),
            _question("What does mutual TLS add compared with server-authenticated TLS?", ("The client also presents a certificate for authentication", "It removes encryption", "It authenticates only DNS servers", "It disables certificate validation"), 0, "Mutual TLS authenticates both the server and the client using certificates."),
            _question("What is a time-of-check to time-of-use (TOCTOU) flaw?", ("A resource changes between a security check and its later use", "A password is hashed twice", "An encrypted file is downloaded slowly", "A certificate expires before issuance"), 0, "An attacker may alter a resource after validation but before the program acts on it."),
            _question("In threat modeling, what does STRIDE stand for?", ("Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege", "Scanning, Testing, Recovery, Inspection, Defense, Encryption", "Storage, Transport, Routing, Identity, Data, Endpoint", "Session, Token, Request, Input, Database, Execution"), 0, "STRIDE is a threat categorization mnemonic used to analyze system designs."),
            _question("What is envelope encryption?", ("Encrypt data with a data key and protect that key with a key-encryption key", "Encrypt a key with the same plaintext repeatedly", "Store plaintext beside a hash", "Use one public key for every operation"), 0, "Envelope encryption separates bulk data encryption from key-encryption-key management."),
            _question("How can signed software artifacts help defend a software supply chain?", ("They allow consumers to verify origin and integrity", "They guarantee source code has no vulnerabilities", "They make dependency updates unnecessary", "They replace access control"), 0, "A trusted signature can show an artifact has not been altered and came from an expected signer."),
            _question("What does DNSSEC primarily provide for DNS data?", ("Origin authentication and integrity for signed DNS records", "Confidentiality of every DNS query", "Protection from all phishing", "User password hashing"), 0, "DNSSEC adds cryptographic signatures to authenticate DNS data and detect tampering."),
            _question("Why is memory-safe software valuable for security?", ("It prevents classes of errors such as many out-of-bounds accesses and use-after-free bugs", "It guarantees correct authorization decisions", "It prevents social engineering", "It eliminates the need for updates"), 0, "Memory-safe languages and designs reduce common memory-corruption vulnerability classes."),
            _question("What is a key risk of relying on a vulnerable transitive dependency?", ("An indirect package may introduce exploitable code into the application", "It makes every request anonymous", "It disables TLS certificate checks", "It guarantees a build will fail"), 0, "Dependencies of dependencies are still part of the software attack surface."),
            _question("What does a key management service commonly provide?", ("Controlled creation, storage, access, and rotation of cryptographic keys", "A replacement for all application authorization", "Automatic correctness proofs for encryption", "Public storage for plaintext passwords"), 0, "KMS systems centralize key lifecycle controls and audit access to key operations."),
            _question("What is a benefit of using a content security policy with restrictive script sources?", ("It can reduce the impact of injected scripts by limiting what may execute", "It prevents all server-side injection", "It validates SQL queries", "It makes passwords unguessable"), 0, "A restrictive CSP limits permitted script sources and can mitigate some XSS consequences."),
        ],
    },
}


def generate_interview(subject: str, difficulty: str, number_of_questions: int = 10) -> list[dict[str, Any]]:
    """Select unique local questions and adapt them to the interview API schema."""
    if not isinstance(subject, str) or subject not in QUESTION_BANK:
        raise ValueError("Choose one of the supported interview subjects.")
    if not isinstance(difficulty, str) or difficulty not in QUESTION_BANK[subject]:
        raise ValueError("Choose a valid difficulty level.")
    if isinstance(number_of_questions, bool) or not isinstance(number_of_questions, int):
        raise ValueError("The number of questions must be a whole number.")

    bank = QUESTION_BANK[subject][difficulty]
    if not 1 <= number_of_questions <= len(bank):
        raise ValueError(f"Choose between 1 and {len(bank)} questions.")

    generated = []
    for item in random.sample(bank, number_of_questions):
        options = list(item["options"])
        random.shuffle(options)
        option_map = dict(zip(LETTERS, options, strict=True))
        correct_answer = next(letter for letter, text in option_map.items() if text == item["answer"])
        generated.append({
            "question": item["question"],
            "options": option_map,
            "correct_answer": correct_answer,
            "explanation": item["explanation"],
        })
    return generated


def generate_questions(subject: str, difficulty: str) -> list[dict[str, Any]]:
    """Compatibility wrapper for callers using the original service function."""
    return generate_interview(subject, difficulty)


def public_question(question: dict[str, Any]) -> dict[str, Any]:
    """Return only question text and options before the candidate submits."""
    return {"question": question["question"], "options": question["options"]}


def evaluate_interview(questions: list[dict[str, Any]], user_answers: list[Any]) -> dict[str, Any]:
    """Score a complete answer sheet and return an itemized review."""
    if not isinstance(user_answers, list) or len(user_answers) != len(questions):
        raise ValueError(f"Please submit answers for all {len(questions)} questions.")
    for index, answer in enumerate(user_answers):
        if answer not in LETTERS:
            raise ValueError(f"Please answer question {index + 1} before submitting.")

    review = []
    correct_count = 0
    for index, (question, selected) in enumerate(zip(questions, user_answers, strict=True), start=1):
        correct_answer = question["correct_answer"]
        is_correct = selected == correct_answer
        correct_count += int(is_correct)
        review.append({
            "number": index,
            "question": question["question"],
            "options": question["options"],
            "your_answer": selected,
            "correct_answer": correct_answer,
            "status": "correct" if is_correct else "wrong",
            "explanation": question["explanation"],
        })

    total = len(questions)
    percentage = round((correct_count / total) * 100, 1) if total else 0
    return {
        "total_questions": total,
        "correct_answers": correct_count,
        "wrong_answers": total - correct_count,
        "unanswered": 0,
        "score": f"{correct_count}/{total}",
        "percentage": percentage,
        "review": review,
    }