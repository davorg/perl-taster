---
title: Perl Taster
subtitle: Your First Two Hours with Perl
edition: Second Edition
author: Dave Cross
language: en-GB
cover-image: cover.jpg
...

Introduction
============

Welcome to Perl. This book is a basic introduction to programming in
Perl. It is intended as a taster that will show you just enough Perl
to enable you to get a feel for the language and to write simple but
useful programs. At the end of the book, you will find pointers to
other resources that you will find useful in order to continue learning
and using Perl.

Perl is a general purpose programming language. It became really popular
for web programming in the 1990s, but it can be just as useful for many
other general programming tasks. Perl borrows heavily from a number of
other programming languages and it has also been heavily influenced by
Unix/Linux utilities like `awk` and `sed`.

If you want to impress people in the Perl community then you should
never refer to the language as “PERL”. Perl is not an acronym (although
possible expansions like “Practical Extraction and Reporting Language”
and “Pathologically Eclectic Rubbish Lister” are often retro-fitted to
the name). The language is "Perl" and the program that you use to run
your Perl code is called "perl".

Getting Started
===============

To write and run Perl programs, you need two things—a Perl compiler
and an editor. This book uses features that were added in Perl 5.36,
which was released in 2022, so you will need that version or a later
one.

If you're using Linux, then Perl will almost certainly already be
installed on your system, and any reasonably recent distribution will
have a new enough version. Macs also come with Perl, but at the time of
writing Apple ships Perl 5.34, which is too old for the code in this
book. The easiest way to get a newer version is to install
[Homebrew](https://brew.sh/) and then run `brew install perl`.

If you're using Windows then you'll need to install Perl. The version
that most people recommend is Strawberry Perl, which you can get from
[https://strawberryperl.com/](https://strawberryperl.com/). It is
distributed as a standard Windows installation file (an .msi file) so
you will be able to install it easily.

Once you have Perl installed, it is simple to check that it is working
correctly. Just open a terminal window (on Windows, that's the Command
Prompt or PowerShell) and run `perl -v` to see which version of Perl is
installed. You're looking for something like "This is perl 5, version
36" or a higher version number.

You will also need an editor to write your Perl programs. Any basic text
editor will do, but as you get more proficient at programming you'll
find that a proper programmer's editor is very useful. Many Perl
programmers use something like Vim or Emacs. These editors both have
quite steep learning curves, so you might feel more comfortable starting
with something like Visual Studio Code, which you can download from
[https://code.visualstudio.com/](https://code.visualstudio.com/).

Your First Perl Program
=======================

It’s traditional that your first program in any language should print
the words “Hello world”. So that’s what we will do. Open your editor and
type in the following:

    #!/usr/bin/perl

    use v5.36;

    print "Hello world\n";

Save the file as `hello.pl` and run it by typing `perl hello.pl` on your
command line. You should see the text “Hello world”. If it doesn’t work,
then the most likely problem is that you aren’t running the command from
the directory where you saved the program. Find the directory where the
`hello.pl` file is and try running the command from there.

There’s not much to explain here. The first line is called the "shebang"
line. On Linux and macOS it tells the operating system which program
should run this file, and Perl itself looks at it for options. You'll
see it at the top of most Perl programs.

The `use v5.36` line tells Perl that this program is written for Perl
version 5.36 or later. Perl takes backwards compatibility very
seriously, so many of the features added in recent years have to be
turned on before you can use them. Asking for a version like this turns
on all of the features that were current in that version, along with
some useful safety checks that we'll look at in a later chapter. Every
complete program in this book starts with this line.

The last line is where the work happens. It calls a built-in Perl
function called [`print()`](https://perldoc.perl.org/functions/print). You can probably guess
what `print()` does—it takes a string and displays that string on the
screen. In this case, we pass it the string “Hello world\n” and that is
what we see on our screen. If you have used pretty much any other modern
programming language you will recognise the final two characters in that
string (the `\n`) as a character sequence that is almost universally
recognised as meaning a newline character. Try removing it from your
string and see what difference it makes when you run the program.

In many other languages you would need to put parentheses around the
string that you pass to Perl—`print("Hello world\n")`—this also
works, but Perl programmers tend to omit non-essential punctuation.

There is another way to write the same program. In fact there are many
other ways (one of Perl’s mottos is “There’s more than one way to do
it”) but we will only cover one more here. Try putting the following
in a file called `hello2.pl` and running it:

    #!/usr/bin/perl

    use v5.36;

    say 'Hello world';

The function [`say()`](https://perldoc.perl.org/functions/say) is a shortcut version
of `print()` which always adds a newline to the end of what it prints.
It is one of the features that `use v5.36` turns on for us. You will
often see `use` statements near the top of a Perl program (the same
keyword is used to load external libraries) and it is traditional to
put them all there.

Strings
=======

You will have noticed that when I used [`print()`](https://perldoc.perl.org/functions/print), I passed it a string in
double quotes, but when I used [`say()`](https://perldoc.perl.org/functions/say) I used a string in single quotes.
And you may be wondering if there is a difference between the two. Perl
treats strings similarly to many other languages. Single-quoted strings
are very basic. Almost every character in a single-quoted string
represents itself and has no special meaning. There are only two
exceptions. A single quote character has a special meaning as it is used
to end the quoted string and a backslash can be used to escape a single
quote so that it doesn’t end the string. Try the following lines:

    print 'Hello world\n';
    print 'Hello 'world'';
    print 'Hello \'world\'';

In the first example, the `\n` is treated as the characters `\` and
`n` rather than as a newline, as that character sequence has no special
meaning in a single-quoted string.

The second example gives a syntax error as the second single quote ends
the quoted string and the following single quotes make no sense.

In the third example, the second and third quotes are escaped with a
backslash and are therefore treated just as single quote characters and
don’t end the string. It is left for the unescaped fourth single quote
to do that.

Double-quoted strings are different. They treat more characters in
special ways. We have already seen the very common `\n` sequence, but
there are many more. For example `\t` is a tab character and `\x{3a}`
is the character whose code is the hex number 0x3A (i.e. a semicolon).
Try the following lines:

    print "This includes a\ttab";
    print "This\nhas\nlots\nof\nnewlines\n";
    print "\x{50}\x{65}\x{72}\x{6c}",
          "\x{20}\x{52}\x{6f}\x{63}",
      "\x{6b}\x{73}\x{21}";

Notice that, in order to stop our line of code getting too long, we
split the string in the last example in two. The `print()` function is
happy to print as many strings as you pass it—they just need to be
separated by commas.

Double-quoted strings have one more trick up their sleeves—they
automatically expand variables. But in order to demonstrate that, we
first need to understand variables.

Variables
=========

Variables are named locations in memory where we can store values that
we want to refer to later. Many programming languages force you to declare
what type of data you will store in a variable (“this variable will store
a string”, “this variable will store an integer”). Perl is more flexible
about this. You can store any kind of data in any variable.

Perl has three main type of variables. Scalars store a single item of
data. Arrays store an ordered list of data items. Hashes store look-up
tables.

Scalars
-------

Try the following code:

    use v5.36;

    my $name = 'John';
    say "Hello $name";

Here we see our first scalar variable. A scalar variable can store a
single piece of data. Our variable is called `$name` and it stores
someone’s name. We define a variable with the keyword `my` and you can
tell that `$name` is a scalar because its name starts with a `$`
character. Whenever you see a `$` in a variable name, you know it
refers to a scalar value.

In this example, we have declared the variable and assigned a value to
it all in the same statement. You don’t have to do that. You can declare
the variable on one line and give it a value later on. It would be just
as valid to write this:

    use v5.36;

    my $name;
    $name = 'John';
    say "Hello $name";

From now on, I'll omit the `use v5.36` line (and the shebang line) from
short examples. When you try them out, please assume that those lines
are part of the code.

This code also has an example of a variable being expanded in a
double-quoted string. When the `say()` statement is executed, Perl looks
at the current value of `$name` and substitutes that value in the string
that is passed to `say()`. So this displays “Hello John”. If you change it
to a single-quoted string, you will see that the variable is no longer
expanded and “Hello $name” is displayed.

Declaring a variable with `my` just tells Perl about the existence of
the new variable. It doesn’t tell Perl anything about the type of data
that we will store in the variable. We can, in fact, store any kind of
data in a variable. Try this:

    my $variable = 'John';
    say $variable;
    $variable = 100;
    say $variable;
    $variable = 3.142;
    say $variable;
    $variable = "\x{3a}";
    say $variable;

In many other languages, you wouldn’t be able to store so many different
types of data in the same variable. You would need to create one
variable for your string, one variable for your integer, one variable
for your floating point number and, perhaps, another for your single
character. In Perl (and other languages in the same family like Python
and Ruby) you can happily store any kind of data in any scalar variable.

If you declare a variable and don't give it a value, Perl knows that its
value is undefined. This is marked with the special scalar value
`undef`. You can return a variable to an undefined state by assigning
`undef` to it directly:

    $variable = undef;

Or by using `undef()` as a function.

    undef $variable;

Note that this special value is unquoted. It is not the string "undef".

Arrays
------

I said that you could store any kind of data in a scalar. It’s more
accurate to say that you can store any single item of data in a scalar.
If you have a list of data items that you want to store, then you need
an array. An array stores an ordered list of scalar values. Try this
code:

    my @numbers = (1, 2, 3, 5, 8, 13);
    say $numbers[0];
    say $numbers[2];
    my @names = ('John', 'Paul',
                 'George', 'Ringo');
    say $names[1];
    say $names[3];

Here, we have created two arrays and populated them using lists of
scalar values. A list is just a sequence of values separated by commas
and surrounded by parentheses. Notice that, as with scalars, we declare
array variables using `my`. Once we have an array we can access
individual elements of it by appending an index number in square
brackets. The first element in the array has the index 0. Notice, also,
that the symbol in front of the variable name changes from a `@` to a
`$`. This is because an individual element in an array is a scalar
value and we always use `$` to refer to scalar values.

In the previous example we had one array that contained numbers and
another that contained strings. But our arrays don't even need to be
that structured. Perl is quite happy for us to mix different type of
data in the same array. They are all just scalar data values. So you can
write something like this:

    my @data = ("\x{3a}", 7,
                'A random string',
                2.718);
    say $data[0];

You can also access elements from the opposite end of the array. The
index -1 refers to the last element of the array. So in our previous
example, we could run:

    say $data[-1];

And Perl would print 2.718.

You can also print all of the elements from an array at the same time by
passing the array as a whole to [`print()`](https://perldoc.perl.org/functions/print) or `say()`.

    say @data;

Doing it like this will give you the string ";7A random string2.718" as
all of the elements are run together. To print it with spaces between
the elements, simply put the array into a double-quoted string.

    say "@data";

Each array has an associated scalar variable which gives the index of
the current final element of the array. To access this variable replace
the `@` at the start of the array's name with `$#`. For an array
called `@data`, this is `$#data`. So our previous example could just
as easily be written:

    say $data[$#data];

Note that because array indexes start from 0, the `$#array` variable
does not give the number of elements the array—its value is one less
than the number of elements. For example in an array with only one
element, the last (and only) index is 0. So the number of elements in an
array is always given by `$#array + 1`.

There is another way to get the number of elements in an array. If you
assign an array to a scalar variable, you get the number of elements.

    my $number_of_elements = @data;

If this is the `@data` array from our previous example, then
`$number_of_elements` will contain 4. This gives us a nice way to add
an element to our array. If the number of elements in an array is always
one more than the last index in that array, then accessing the element
at that position, will give us an element that is outside of the
existing array. But Perl allows us to assign a value to this
non-existent element and resizes the array for us.

    $data[$number_of_elements] = 'A new value';

Our array now has a new, fifth, element containing the string 'A new
value'. And we don't need to stop at the element just off the end of the
current array. We can assign values to any non-existent element and Perl
will grow the array accordingly. So if we ran:

    $data[999999] = 'Another new value';

We will suddenly have an array that contains a million elements. All of
the elements that we haven't explicitly given values to (that's all of
them except the first five and the last one) will contain the value
`undef`.

You can also shrink an array easily. You can write to the `$#array`
variable and it will change the size of the array directly. Any
values that previously existed at indexes beyond the new final index
of the array will vanish.

Hashes
------

The final variable type that we will cover is the hash. Hashes are a bit
like arrays in as much as they store a scalar value against a key so that
you can retrieve it later. But whereas array keys are an ascending
sequence of integers, hash keys are arbitrary strings. This makes them
good for storing look-up tables, but means that they don't have any kind
of implicit ordering. You can't expect to get values out of a hash in
the same order as you put them in.

Like arrays, you initialise hashes with lists. But Perl it needs to be a
list containing an even number of element (a key and value for each
element in the hash) and you will get a warning from Perl if there are
an odd number of items in your list.

    my %french = ('one', 'un',
                  'two', 'deux',
                  'three', 'trois');
    say $french{'two'}; # prints "deux";

Looking up data in a hash looks a lot like looking up data in an array.
You just use a different type of brackets (curly braces instead of
square brackets) and the key is a string rather than an integer. The
symbol in front of the hash name changes from a `%` to a `$` for
exactly the same reason that a similar change takes place with arrays—because a what you get back from the hash lookup expression is a single
scalar value.

This syntax for initialising a hash works, but it can be difficult to
see where one key/value pair ends and the next one starts. For this
reason, Perl also has an alternative syntax using a "fat comma"
operator. It looks like this:

    my %french = (one => 'un',
                  two => 'deux',
                  three => 'trois');
    say $french{two}; # prints "deux";

Notice how the `=>` operator really emphasises the link between the
key/value pairs. Notice, also, that we can drop the quote marks around
the keys. This is because the fat comma operator automatically quotes
the value on its left-hand side. Of course, if your key contained a
space, then the auto-quoting wouldn't work and you would need to go back
to quoting the key. We can also omit the quotes around the key when we
use it in the the `{ … }` lookup brackets. These brackets follow the same
auto-quoting rules as the fat comma (and are subject to the same
restrictions.

You can add new values to a hash by just assigning a value to a new key.

    $french{four} = 'quatre';

If the key doesn't already exist in the hash, then Perl will create a
new key and associate your value with it. If the key already exists,
then Perl will overwrite the existing value with your new one. You can
only ever have one scalar value associated with any given key.

There is an [`exists()`](https://perldoc.perl.org/functions/exists) function which can tell you if a given key exists
in your hash.

    say exists $french{five};

This will print either 1 (if the key exists) or an empty string (if it
doesn't). We will cover this in more detail when we look at logic in
Perl.

You can delete keys from a hash with the [`delete()`](https://perldoc.perl.org/functions/delete) function. You will get
the value associated with the deleted key returned to you.

    say exists $french{three}; # prints 1
    my $three = delete $french{three};
    say exists $french{three}; # an empty string

Getting Help
============

There is plenty of help available when you are writing Perl code and you
should take advantage of it as much as possible.

Documentation
-------------

Perl comes with an incredible amount of detailed documentation which you
can access from your command line using the `perldoc` command. For
example `perldoc perlintro` gives a brief introduction to Perl and
`perldoc perltoc` shows you a table of contents for all of the available
documentation. You can also access this documentation online at
[https://perldoc.perl.org/](https://perldoc.perl.org/).

In particular, I would recommend reading `perldoc perlfaq` and all of the
other FAQ documents that it points to. They contain a treasury of
information that will undoubtedly make your Perl programming easier.

All of Perl's built-in functions are documented in `perldoc perlfunc`.
But if you know the name of a function and you want to quickly get the
documentation for that function, you can use the `-f` flag to `perldoc`.
For example, `perldoc -f print` will tell you everything that you need
to know about [`print()`](https://perldoc.perl.org/functions/print).

Safety Nets
-----------

Perl has two "safety nets" that make it run extra checks on your code
and tell you if it finds anything that doesn't look right. They are
called `strict` and `warnings`. Taking notice of the problems they
report and making the suggested fixes will almost certainly fix
potential bugs in your code.

If you have been following along, you're already using them. The
`use v5.36` line at the top of our programs turns both of them on. In
older Perl code you will see them turned on explicitly, with two lines
near the top of the program:

    use strict;
    use warnings;

You don't need those lines if your program starts with `use v5.36`, but
it's useful to recognise them, as you'll see them in almost every Perl
program written before 2022.

The most important thing that `strict` does is to force you to declare
your variables. This is a good idea for several reasons, the most
obvious of which is that it stops you from making typos in your
variable names. If Perl knows that you have declared all of your
variables and then comes across an undeclared variable called
`$varaible` then the compiler knows that something is wrong. It won't
know that you meant the variable called `$variable` which you have
declared, but, hopefully, if it shows you the error you can work out
what has gone wrong. Most of the problems that `strict` finds are
treated as fatal errors, so Perl shows you the error and then stops the
program.

With `warnings` turned on, Perl goes on the lookout for a large number
of unusual coding practices. Are you printing a variable that contains
`undef`? Perl will warn you. Have you initialised a hash from a list
with an odd number of elements? Perl will warn you. In all of these
cases, Perl won't stop the program—it will display a warning and the
program will continue. But you would be well-advised to take note of
the problem and fix it.

If you get a warning that you don't quite understand, then it can be
useful to add `use diagnostics` to your program as well. This will
display a far longer explanation of the problem along with some likely
solutions. But don't leave that line in your code when it goes into
production.

All in all there are no good reasons not to use these safety nets.
That's why experienced Perl programmers use them all the time.

Input and Output
================

Programs get more interesting when you can get data into and out of
them. Before moving on to look at more operators and functions,
let's take a quick aside to look at some simple I/O methods.

When a program runs, your operating system will open three file handles
that you can use to interact with the console. There is one called `STDIN`
which is connected to the keyboard. You can read from this to get input.
There is one called `STDOUT` which is connected to the monitor. You can
write to this to display output. The third file handle is called `STDERR`.
It is a writable file handle like `STDOUT` and it should be the place
where you write warnings and errors. By default, like `STDOUT`, it is
connected to the monitor.

Output
------

We have already seen the simplest way to display output to the user—it's the [`print()`](https://perldoc.perl.org/functions/print) function.

You can pass one or more strings to `print()` and they will be displayed
on the user's monitor.

    print "Here is a string\n";
    print "Here are", "two strings\n";

If you want to pass more than one string to `print()`, then you separate
them using commas.

We have also seen the [`say()`](https://perldoc.perl.org/functions/say) function which works very similarly to
`print()`, except it automatically appends a newline character to the end
of the final sting that it prints.

    say "Here is a string";
    say "Here are", "two strings";

Input
-----

Input is read from `STDIN`. You read from a filehandle using the file
input operator, `< … >`. The file input operator reads from the
given file handle and returns the data up to and including the next
newline character.

    print "What is your name? ";
    my $name = <STDIN>;
    print "Hello, $name";

Here, we prompt the user for their name (note that there is no newline
so the cursor will stay just after the question mark at the end of the
prompt). The program then pauses, waiting for input on `STDIN`. The user
gives us input by typing on the console and pressing the return key. We
won't get any input until the return key is pressed but, once it is, we
will get all of the data that the user typed in including the newline
character. We can then store that data in a variable and then print out
the value of the variable. Notice that as `$name` contains all of the
data, including the newline on the end, we don't need to supply our own
newline character in the print statement.

But what if we didn't want that newline? Perhaps we want our print
statement to look like this.

    print "Hello, $name. ",
          "Pleased to meet you.\n";

As it stands, this will print the output over two lines. `$name` still
has a newline in it, so the full stop and the "Pleased to meet you" will
be pushed onto the following line. Perl, of course, has a simple
solution to this problem. You can use the [`chomp()`](https://perldoc.perl.org/functions/chomp) function to remove a
newline from the end of a string. so our code will look like this:

    print "What is your name? ";
    my $name = <STDIN>;
    chomp $name;
    print "Hello, $name. ",
          "Pleased to meet you.\n";

The last standard file handle is `STDERR`. This is where you should send
any errors and warnings. At the level we are covering in this tutorial,
this won't be any different to sending them to `STDOUT`, but it's a good
habit to get into for the future.

You can print to `STDERR` using `print()` or `say()`. They both take an
optional first argument which is the filehandle to print to. It's a
slightly strange first argument as there is no comma following it. So
you could write something like this:

    # Note: No comma
    print STDERR "Something went wrong\n";

But Perl has a shortcut function called [`warn()`](https://perldoc.perl.org/functions/warn) that you can use instead.

    warn "Something went wrong\n";

Operators and Functions
=======================

Perl has a vast array of operators and functions that allow you to
manipulate your data in various ways. In a short tutorial like this we
can't hope to cover all of them, but we can explain some of the most
common ones.

Arithmetic Operators
--------------------

Perl has operators for all of the standard arithmetic operators—addition, subtraction, multiplication and division.

    my $addition       = 9 + 5; # 14
    my $subtraction    = 9 - 5; #  4
    my $multiplication = 9 * 5; # 45
    my $division       = 9 / 5; #  1.8

It also has operators for less common operators. For example `**` is
the exponentiation operator ("raising to the power of").

    my $power = 9 ** 5; # 59,049
                        # (9 x 9 x 9 x 9 x 9)

And `%` is the modulus operator. This carries out an integer division
and returns the remainder.

    my $modulus = 9 % 5; # 4 (9/4 is 1 remainder 4)

All of these operators are also available in a shortcut assignment
versions.

    $sum     += $value; # $sum = $sum + $value
    $product *= $value; # $product =
                        # $product * $value

There is another, even simpler, version of the shortcut addition and
subtraction operators if you are adding or subtracting 1. You can use
`$variable++` to increase the value by 1 and `$variable--` to decrease it
by 1.

Other Operators
---------------

You can concatenate two strings together with the `.` operator.

    my $name = $forename . ' ' . $surname;

But that would more commonly be written as

    my $name = "$forename $surname";

There is a shortcut assignment version.

    my $page .= $line; # Same as $page = $page . $line

There is also a string repetition operator—`x`. It repeats its left-hand
operand the number of times given by its right-hand operand.

    say 'hello' x 3; # prints 'hellohellohello'

In thirty years of writing Perl, I've never used that for anything
other than creating separators in reports.

    say '-' x 80;

If the left-hand operand for `x` is a list (which means it is enclosed
in parentheses) then `x` becomes a list repetition operator.

    my @numbers = (1, 2, 3) x 3;
    say @numbers; # prints 123123123

Branching and Looping
=====================

Code gets a lot more useful when you can take different routes through
it. Before we can talk in detail about decision points, we need to get a
grounding in basic logic.

True and False
--------------

Many programming languages have explicit "true" and "false" values. Perl
doesn't take that approach. Instead, in Perl, any expression can be
evaluated to give a "truth value". That is, any expression can be either
true or false. To do this, Perl declares that a small number of values
are false. All other values are assumed to be true. The false values
are:

* The number `0` (and `0.0`)
* The string `"0"`
* The empty string
* The empty list, `()`
* The undefined value

Any other value is true. With that in mind we can examine some
expressions and decide whether they are true or false.

* `0`: false (it's on the list)
* `1`: true (it's not on the list and is therefore true)
* `"0.0"`: true (it's not on the list and is therefore true. Note that
"0.0" is not "0")
* `"false"`: true (it's not one of the list of false values)
* `(3 * 2) - 6`: false (it evaluates to 0, which is on the list)

If, else and while
------------------

Now that we understand how we can work out if a value is true or false,
we can start to take different actions. We do this using the `if … else …`
statement.

Imagine writing a game, where we have a variable called `$lives_left`
containing the number of remaining lives. When the player does something
which causes him to lose a life you will see code that looks something
like this:

    if ($lives_left) {
      say "Have another try.";
      $lives_left--;
    } else {
      die "Game over\n";
    }

Let's assume that `$lives_left` starts at 3. Then the first time this
code is run, the expression in the `if` statement is true (`$lives_left`
is 3 and that's not one of the false values, so it must be true). When
the expression is true, Perl executes the code in the first block. It
prints "Have another try" and decreases the value in `$lives_left` by
one. A couple of failed attempts later, we will run this code when
`$lives_left` has the value 0. That's one of the false values, so the `if`
expression is false and it's the second block of code that gets run—the block that ends the program.

This code actually reads a lot like English—"if this expression is
true then do this, otherwise do that".

Sometimes you don't need the `else` part of the code. That's fine, you
can just omit it.

    if ($some_value) {
      # do something
    }

Sometimes you might have more complex logic which you can implement with
added `elsif` sections (be careful of the spelling of "elsif").

    if ($some_value) {
      # do something
    } elsif ($some_other_value) {
      # do something else
    } else {
      # do something completely different
    }

An if statement has one `if`, as many `elsif`s as you want and zero or
one `else`.

In our game example above, I talked about the code being called several
times. This implies that there is some kind of loop around all of the
previous code. At a simple level, the loop might look something like
this:

    my $lives_left = 3;
    while ($lives_left) {
      # Do something that sets $died
      # to a true or false value
      if ($died) {
        if ($lives_left) {
          say "Have another try.";
          $lives_left--;
        } else {
          die "Game over\n";
        }
      }
    }

We initialise `$lives_left` to 3 and then go into a while loop. The
`while` loop works a lot like an `if` statement, but it does it repeatedly.
If the expression in the `while` loop is true then the code block is
executed. The difference is in what happens after the block has
executed. With an `if` statement, the next statement after the end of
block is executed. But with a `while` loop, the `while` expression is
checked again and if it is still true then the block is executed again.
This continues until the expression is false.

Comparison Operators
--------------------

Another common requirement is to compare two values to see if they are
equal or not. Perl has a set of operators for doing this. In fact it has
two sets of these operators for reasons that we will see soon.

Imagine you are programming a thermostat. The code is pretty simple, all
you do is check the temperature and if it is below a certain level, then
you turn on the heating. It would look like this:

    if ($current_temp < $too_cold) {
      # turn on heating
    }

Here we're using the `<` operator which you probably remember from
maths lessons. If `$current_temp` is less than the value in `$too_cold`
then the expression is true and the if block is executed. There's a
greater than comparison too—the easy way to remember which is which is
that the arrow points towards the smaller value. If our heating system
also has built-in air conditioning, then we can use a greater than test
to turn that on if the temperature gets too high.

    if ($current_temp < $too_cold) {
      # turn on heating
    } elsif ($current_temp > $too_hot) {
      # turn on aircon
    }

Perl also has operators that can be used to check if two values are
equal (`==`), not equal (`!=`), less than or equal to (`<=`) and greater
than or equal to (`>=`). Between them, they should cover all
possibilities.

Those operators are used to compare numbers. You can remember that
because they look like maths symbols. Perl has another set of operators
for comparing strings. We need another set because Perl automatically
converts between numbers and strings so sometimes it needs the
programmer to tell it how values need to be compared.

As an example, say you wanted to compare two variables and those two
variables contained the values "0" and "0.0". Are those values the same?
The answer is "it depends". If you compare the values as numbers, then
they are the same (0 and 0.0 are clearly the same number—given that
Perl doesn't see a difference between integers and real numbers). But if
you treat them as strings, then they are different—they have different
lengths, for example. Perl can't know which type of comparison, so you
need to tell it.

    # Compare as numbers
    if ($one_value == $another_value)
    
    # Compare as strings
    if ($one_value eq $another_value)

All of the numeric comparisons we saw above have string equivalents. The
complete list is `eq` (equal), `ne` (not equal), `lt` (less than), `gt`
(greater than), `le` (less than or equal to) and `ge` (greater than or
equal to). When comparing strings it is done by comparing the individual
letters in the strings. So "apple" is less than "banana" because "a" comes
before "b" in the character set that Perl uses. This looks like it is
alphabetical order, but don't be fooled. The upper case letters appear
in the character set before the lower case ones do, so "Banana" is less
than "apple".

At some point in your Perl programming career, you will use the wrong
comparison operators. This is one of the reasons that `warnings` are so
useful. If you try to compare strings that don't look like numbers
using the numeric comparison operators, then Perl will give you a
warning.

Combining Logical Expressions
-----------------------------

Sometimes, driving our logic from the result of one expression isn't
enough and we will need to combine two or more expression in order to
get a result. We have the `&&` (and) and `||` (or) operators for this.
You can also use the actual words `and` and `or`.

For example, imagine that the thermostat we were talking about earlier,
only needed to turn the heating on if it was the weekend (because we're
out of the house during the week). To code would look like this:

    if (($current_temp > $too_cold)
      and (($day eq 'Sat')
        or ($day eq 'Sun'))) {
      # turn on heating
    }

We have three conditions that we are checking here. There's the original
check for the temperature, but there are also two new checks for the
day. The two day checks are joined together with `or` as only one of
them can ever be true and we know it's the weekend if either of them is
true. The day checks are combined with the temperature check using `and`
as we need both of these conditions to be true. Notice that we have used
parentheses around the expressions. This ensures that Perl interprets
the combination of conditions as we want. A Perl expert would be able to
rewrite these expressions so they work without the parentheses, but it
doesn't hurt to be over-cautious. Let's simplify the expressions so we
can see how they are combined.

    (temperature_check) and
      ((saturday_check) or (sunday_check))

And that simplifies even more to

    (temperature_check) and (weekend_check)

These `and` and `or` operators are included in most programming
languages. They take two logical expressions and combine them into a
single expression according to simple rules. The `and` operator returns
true only if both of its expressions are true and the `or` operator
returns true if either (or both) of its expressions are true.

Perl's logical operators are lazy. That, they only do as much work as
necessary in order to work out the value of the combined expression. If
you have an expression `A and B`, Perl will start by evaluating `A`. If `A`
is true, then Perl needs to evaluate `B` to calculate the final result.
But if `A` is false, then it doesn't matter what `B` is. The result already
has to be false. Therefore Perl doesn't bother to evaluate `B`. Similarly,
if the expression is `A or B` and `A` is true, then there is no reason to
evaluate `B`—as the combined expression must be true.

A huge amount of programming is about getting these combinations of
logical expressions right, so it's worth checking carefully whenever you
write one.

Built-In Functions
==================

Perl has a number of built-in functions that you can use in your
programs. We have already seen examples like [`print()`](https://perldoc.perl.org/functions/print), [`say()`](https://perldoc.perl.org/functions/say) and [`chomp()`](https://perldoc.perl.org/functions/chomp).
There are dozens of them and in this section we can only cover a few.
You can find the full list by reading the `perlfunc` manual page.

Numeric Functions
-----------------

Perl has many of the numeric functions that you will remember from
school. For example, there is a [`sqrt()`](https://perldoc.perl.org/functions/sqrt) function that returns the square
root of a number.

    say sqrt 25; # Displays 5
    say sqrt 2;  # Displays 1.4142135623731

There is an [`abs()`](https://perldoc.perl.org/functions/abs) function which gives the absolute value of an
expression. That means that if the expression is negative, then `abs()`
will drop the minus sign before returning the value to you. This is
useful, for example, if you want to find the difference between two
values and you don't know which is the largest.

    my $difference = abs $value -
                         $another_value;

It is often useful to generate a random number and Perl has the [`rand()`](https://perldoc.perl.org/functions/rand)
function for this. With no arguments, it returns a random floating point
number that is between 0 and 1 (actually, just less than 1).

    say rand; # I got 0.711371782775135,
              # you probably won't

In our game, if a player has a 50% chance of dying at some point, you
could use this:

    my $died = rand > 0.5;

The variable `$died` will be set to a true value if `rand()` gives you a
number greater than 0.5—which it will do 50% of the time.

You can also pass a number to `rand()`, and you will then get a random
number between 0 and just less than the number you passed in.

    print rand 20; # I got 6.85922801176282

You can use this together with [`int()`](https://perldoc.perl.org/functions/int) (which truncates floating point
numbers to integers) to simulate dice.

    say int(rand 6) + 1;

Calling `rand 6` gives a floating point number between 0 and just under
6. Truncating that to an integer gives a number between 0 and 5. Adding
one to that gives a dice throw.

String Functions
----------------

The next set of functions we will look at work on strings. The simplest
is probably [`length()`](https://perldoc.perl.org/functions/length) which gives you the length of the string.

    say length 'This is a string'; # Displays 16

You change the case a string with [`uc()`](https://perldoc.perl.org/functions/uc) (convert to upper case) and [`lc()`](https://perldoc.perl.org/functions/lc)
(convert to lower case).

    say uc 'This is a string'; # THIS IS A STRING
    say lc 'This is a string'; # this is a string

You can extract sections of a string using [`substr()`](https://perldoc.perl.org/functions/substr). You pass this
function a string, a place to start and the length of the substring that
you want. Note that the start of the string is position 0 (this is
similar to arrays).

    say substr 'This is a string', # his
               1, 3;
    say substr 'This is a string', # string
               6, 10;

You can omit the third argument, in which case, the substring goes to
the end of the original string.

    say substr 'This is a string', 10; # string

Two particularly functions are [`split()`](https://perldoc.perl.org/functions/split) (which turns strings into lists
of values) and [`join()`](https://perldoc.perl.org/functions/join) (which does the reverse). Imagine that you have a
date in YYYY-MM-DD format and you want to split it into its constituent
parts.

    my ($year, $month, $day)
      = split /-/, '2015-08-01';

The first argument to `split()` defines the characters that you want to
split on. It is actually a regular expression. Later on, we will see
that this makes `split()` rather powerful.

Sometimes you won't know how many data items there are in the string
that you are splitting. In that case you could store the resulting list
in an array

    my @values = split /\t/,
      $tab_separated_data;

Where `split()` takes a string and converts it into a list of values,
`join()` does the opposite.

    my $date = join '-',
      $year, $month, $day;
    my $tab_separated_data
      = join "\t", @values;

Array Functions
---------------

There are a number of functions that allow you to manipulate arrays.

To add data to the end of an array, use [`push()`](https://perldoc.perl.org/functions/push)

    my @words = ('this', 'is', 'an', 'array');
    push @words, 'with', 'more', 'words';
    say "@words";

To get the last element from an array (and remove it from the array),
use [`pop()`](https://perldoc.perl.org/functions/pop);

    my $word = pop @words;
    say $word;    # "words"
    say "@words"; # "words" is now missing

We also have [`shift()`](https://perldoc.perl.org/functions/shift) and [`unshift()`](https://perldoc.perl.org/functions/unshift) which do the same as `pop()` and `push()`,
but work on the start of the array rather than the end.

    my @words = ('an', 'array', 'of', 'words');
    unshift @words, 'add', 'words', 'to';
    say "@words";
    my $word = shift @words; # "add"
    say "@words";            # "add" is missing

File Functions
--------------

We've talked about simple input and output, but there's a lot more to
deal with when you're reading data from files. To read from or write to
a file, you need to create a file handle. You do this using the [`open()`](https://perldoc.perl.org/functions/open)
function.

    open my $file_handle, '<',
         'name_of_your_file';

This creates a file handle (in a variable called `$file_handle`) that
you can use to read from the file. The `<` means that we have opened
the file in read mode. We can read from the file, but not write to it.

The `open()` function returns a true or false value which indicates
whether the file was opened successfully. If the open wasn't successful,
there is no point in trying to read anything from the file, so you will
very often see code like this:

    open my $file_handle, '<', 'name_of_your_file'
      or die "Could not open file: $!";

We're making good use of the laziness of Perl's logical operator's
laziness that we discussed earlier. We have two expressions combined
with an `or`. If the first expression (the call to `open()`) is true (i.e.
the file was opened successfully) then the whole expressions must be
true and there is no need for Perl to evaluate the second expression.
But if the first expression is false (i.e. the open operation failed)
then Perl needs to evaluate the second expression to find out the value
of the combined expression. Evaluating the second expression calls [`die()`](https://perldoc.perl.org/functions/die)
which kills the program with an error message. The `$!` in the error
message is a special internal Perl variable which will contain an
explanation of why the file could not be opened—so it will say
something like "No such file or directory". This `open … or die …` construct is
incredibly common in Perl programs. You will see it in most Perl code
that you look at.

Having created a file handle, we read from the file using the same
`<...>` operator that we used to read from `STDIN`.

    my $data = <$file_handle>;

This works exactly the same way as when we were reading from `STDIN` (as
you would expect, as `STDIN` is just a file handle that the operating
system has already opened for us). Importantly, the data that ends
up in `$data` will have the newline character on the end and we can use
`chomp()` to remove it.

It is very common to read every line from a file in turn using a while
loop.

    while (<$file_handle>) {
      chomp;
      # Your data is in $_
    }

Each time round this loop, Perl reads a line from the file handle and
puts it into a special Perl variable called `$_`. `$_` is known as the
"default variable" and often Perl functions and operators will work on
`$_` if no other argument is given. We see an example of this here, as
`chomp()` is called with no argument. It will therefore work on `$_` and
remove the newline from that variable.

Experienced Perl programmers make heavy use of `$_`. If you read a piece
of Perl code and it seems to be missing a variable, then it's probably
using `$_`. Most uses of `$_` are invisible—like the `chomp()` example
above.

Eventually you will have read every line from your file. At that point,
the next time that the while loop expression is checked, the `< ... >`
will return `undef`. That is, of course, a false value and the while
loop will end.

As well as reading from files, you will also want to write to files. You
still do this using a file handle, but you need to open the file in
write mode. This is done using the same `open()` command, but we reverse
the direction of the second operator to indicate that we are writing
rather than reading.

    # '>', not '<'
    open my $file_handle, '>',
      'name_of_your_file'
      or die "Could not open file: $!";

We write to the file handle using `print()` (or `say()`), which has an
optional first argument telling it which file handle to print to

    print $file_handle $some_data;

Note that there is no comma between the file handle argument and the
data. This is important as it allows the Perl compiler to know that the
first argument is a file handle, and not data to send to `STDOUT`.

This operation is destructive. Any writes to this file handle will
overwrite any data that already exists in the file. Sometimes, you want
to add new data to the end of a file. If you open a file handle using
`>>` instead of `>` then any data will be appended to the end
of the file rather than overwriting it.

    # '>>', not '>'
    open my $file_handle, '>>',
      'name_of_your_file'
      or die "Could not open file: $!";
    print $file_handle $some_data;

You can use [`close()`](https://perldoc.perl.org/functions/close) to close a previously opened file handle.

    close $file_handle;

Subroutines
===========

A subroutine is a self-contained chunk of code which can be called from
anywhere within your program. In Perl, a subroutine is defined using the
keyword `sub` followed by a name and a block of code.

    sub do_something_useful {
      # code goes here
    }

You can then call this subroutine by giving its name followed by a pair
of parentheses.

    do_something_useful();

The parentheses often aren't necessary, but they are useful to make sure
the compiler knows you are calling a subroutine—so I like to include
them. You will sometimes see subroutines called using an ampersand:

    &do_something_useful;

But that is almost never necessary and I don't recommend using this
syntax.

Here is a subroutine for saying hello.

    sub say_hello {
      say 'Hello';
    }

You can call it like this:

    say_hello(); # "Hello"

It would be nice if we could personalise this and say hello to specific
people. For this we need to pass parameters into the subroutine. We do
that by giving the subroutine a *signature*: a list of variables, in
parentheses, between the subroutine's name and its block of code.

    sub say_hello ($name) {
      say "Hello $name";
    }

We can now call the subroutine like this:

    say_hello('Dave'); # "Hello Dave"

When the subroutine is called, the value that we pass in is copied into
the variable `$name`, which we can then use inside the subroutine just
like any other variable. Notice that we have changed the single quotes
to double quotes so the variable gets expanded.

Signatures are another of the features that `use v5.36` turns on for
us. As well as making the code easier to read, they check that the
subroutine has been called correctly. If you call `say_hello()` with no
arguments, or with two, Perl will stop the program and tell you that
you passed the wrong number of arguments.

A subroutine can, of course, take more than one parameter. Just list
them all in the signature, separated by commas.

    sub say_greeting ($greeting, $name) {
      say "$greeting $name";
    }

    say_greeting('Good morning', 'Dave');

You can also make the last parameter an array. That array will collect
all of the remaining arguments, however many there are. So we can
rewrite our subroutine so that it says hello to as many people as we
like.

    sub say_hello (@names) {
      foreach my $name (@names) {
        say "Hello $name";
      }
    }

Here, we use a `foreach` loop to process each element of the array in
turn. We haven't seen the `foreach` loop before, but it's a useful way
to traverse a list. We define a new variable (here called `$name`) and
each element from the list in turn gets put into that variable. We then
execute the attached block of code for each value in the list. So we can
now call our subroutine like this:

    say_hello('Christopher', 'David', 'Matt',
              'Peter', 'Jodie');

And it will display:

    Hello Christopher
    Hello David
    Hello Matt
    Hello Peter
    Hello Jodie

The list of values that you pass in can be as long as you like.

Signatures were only added to Perl fairly recently, so you will see a
lot of code that doesn't use them. In older code, the arguments to a
subroutine are put into a special array called `@_`, and the first line
of the subroutine usually copies them into variables:

    sub say_hello {
      my ($name) = @_;
      say "Hello $name";
    }

Notice the parentheses around `$name`. Remember that if you assign an
array to a scalar variable, you get the number of elements in the
array. The parentheses turn this into a list assignment, so the first
element of `@_` is copied into `$name`. You don't need to write code
like this yourself, but you'll need to recognise it when you read other
people's Perl.

It is often useful to return values from subroutines. Perl has the
[`return()`](https://perldoc.perl.org/functions/return) function for doing this. In our game, suppose we want to write
a subroutine that works out if a player has died at a particular point.
We can use `rand()` in a subroutine like this:

    sub has_died ($name) {
      if (rand > 0.5) {
        say "$name has died";
        return 1;
      } else {
        return;
      }
    }

There isn't much here that we haven't already seen. We call the
subroutine, passing in the name of a player and use `rand()` to give that
player a 50% chance of dying. If the player has died we display that
information and return a true value (here, a 1). If the player hasn't
died we just call `return()` without passing it a value. That's because if
you don't give `return()` a value, it will return a false value.

We can now call this subroutine like this:

    if (has_died('Matt')) {
      $lives_left--;
    }

And you can see how this will now tie in with the rest of the game code
that we wrote earlier.

But Perl subroutines can return more than one value. You can return a
list of values, which makes it possible to write subroutines like this:

    sub has_died (@names) {
      my @died;
      foreach my $name (@names) {
        if (rand > 0.5) {
          push @died, $name;
        }
      }
      return @died;
    }

This subroutine expects to be passed a list of players' names and gives
each of those players a 50% chance of dying. It then returns a list of
the players that have died. Can you follow how it does that?

Regular Expressions
===================

The final major Perl feature that we will look at is regular expressions
("regexes" for short). Perl has a reputation for being a powerful
language for text processing and it's regexes that give it a lot of that
power.

The name "regular expressions" make the feature seem more complex than
it is. Basically, what we are talking about here is pattern matching.
Regexes give you a mini-language which you can use inside Perl to match
strings in a really flexible way.

Matching is carried out using the match operator, which looks like this:

    if ($string =~ m/some text/) {
      # do something
    }

It's the `m/.../` which is the match operator. We've also introduced the
binding operator (`=~`) which means "match against this string". So the
whole expression here means "look at `$string` and see if it matches this
regex"). The match operator returns a true or false value, so it's
common to use it in an `if` statement as we have here.

The regex itself is the bit between the slashes in `m/.../`. In this
example it is the string "some text". That's a rather simple example as
all of the characters match themselves—so this means "does `$string`
contain the string of characters 'some text'". Note that this is
different to the `eq` operator which checks that to strings are
identical. Here we are checking that one string is contained within the
other. So if `$string` contained "Here is some text", then the regex
would still match it.

An experienced Perl programmer would probably write this example in a
slightly streamlined manner. You might see code like this:

    if (/some text/) {
      # do something
    }

Two things have changed here. Firstly, we have lost the `m` from
`m/.../`. It is optional, so most people omit it. Secondly, we are no
longer explicitly matching against a particular string using `=~`. The
match operator works against `$_` if it is given no explicit input and
many Perl programmers like to take advantage of this. It's surprising
how often the thing you want match against is already in `$_` anyway.
One particularly common use is in a while loop.

    while (<$some_file_handle>) {
      if (/some regex/) {
        # do something
      }
    }

Reading from a file handle in a while loop like this puts the data into
`$_`. So using the match operator's implicit matching against `$_` is a
good idea in this case.

Regexes containing ordinary letters can only get you so far. The true
power of regexes comes through the use of "metacharacters". These are
characters that have special meanings in a regex. The first
metacharacters we will look at allow you look for optional or multiple
characters in a string. A `?` following a character matches zero or one
occurrence of the character, a `*` means zero or more occurrences and a
`+` means one or more occurrence. Here are some examples.

    /colou?r/  # matches both "color"
               # and "colour"
    /colou*r/ # matches "color", "colour",
               # "colouur", "colouuur", etc
    /colou+r/  # matchs "colour", "colouur",
               # etc, but not "color"

If you want to turn off a metacharacter's special meaning and just match
itself then you can escape it by preceding it with a backslash. So `\?`
will match a question mark.

The next set of metacharacters match predefined groups of characters.
You can use `\d` to match any digit, `\s` to match any whitespace
character or `\w` to match any word character (by which, Perl means any
of the characters that you can use in the name of a subroutine—letters, numbers and the underscore). These sequences all have their
inverse, so `\D` matches any non-digit, `\S` matches a non-whitespace
character and `\W` matches a non-word character. A dot can be used to
match any character (except a newline).

    /\d+/        # matches one or more
                  # digits
    /\d+\.\d+/ # matches a floating
                  # point number
    /\w+\s\w+/ # matches two words
                  # separated by whitespace

You can create your own set of characters (called a "character class")
using the `[ … ]` syntax. Just list the characters that you want to
match between the brackets. You can use `-` to denote a range of
characters. Use `^` as the first character in a character class to
invert its meaning and match anything not in the class.

    /[aeiou]/ # Matches any vowel
    /[a-z]/   # Matches any lower-case
              # letter
    /[^a-z]/  # Matches anything that isn't
              # a lower case letter

The last metacharacters we will look are known as "anchors" as the tie
the match to a particular position in the string. To match the start of
a string use `^` and to match the end of the string use `$`.

    /^Some text/ # Matches "Some text" at
                 # the start of your string
    /Some text$/ # Matches "Some text" at
                 # the end of your string

More Information
================

We have covered a lot in this introduction, but there's a lot of material
that we haven't had the space to cover. Here are some suggestions for
other topics to investigate along with the perldoc manual pages that you
can read to get more information.

* `perlintro` is a short overview of the whole language. It's a good
next step after this book.
* We only touched on a few of Perl's built-in functions and operators.
The `perlfunc` and `perlop` manual pages give you the full lists.
* We mentioned a couple of Perl's special variables, but there are
dozens more. The `perlvar` manual page has all of them.
* Regular expressions do a lot more than we talked about. There's a
good tutorial in `perlretut` and a full reference manual in `perlre`.
* Subroutines (and their signatures) can do a lot more than we have
covered. The details are in `perlsub`.
* Perl comes with a lot of useful add-on modules which can be used in
your program. They are all listed in `perlmodlib`. Thousands more are
available from CPAN, the Comprehensive Perl Archive Network, which you
can search at [https://metacpan.org/](https://metacpan.org/).

I hope that this brief introduction has whetted your appetite and
started to show you what a powerful and flexible language Perl is.
There's a lot more to learn so please look for a good course or book to
take your Perl programming to the next level.

About Stuff {.unnumbered}
=========================

About this Book
---------------

This is the second edition of *Perl Taster*. The text and all of the
examples have been updated for Perl 5.36, which means the code now uses
`use v5.36` and subroutine signatures.

The book is written in Markdown. The ebook is built from that source
using pandoc, and the paperback using pandoc and XeLaTeX.

The source to the book is available on GitHub. See
[https://github.com/davorg/perl-taster](https://github.com/davorg/perl-taster).

About Perl School
-----------------

Perl School was an idea that Dave Cross had in 2012. He thought that more
people would attend Perl training courses if they were a) cheaper and
b) at the weekend. This worked for a while, but after six months or so,
the idea (along with the brand) was quietly dropped.

The brand has since been resurrected as a publishing imprint for books
about Perl. *Perl Taster* was its first book.

About the Author
----------------

Dave Cross has been a professional programmer since 1988 and has been
using Perl since 1996. In 1998 he started the London Perl Mongers, the
first Perl Users' Group outside of North America.

Dave is the author of *Data Munging with Perl* and a co-author of
*Perl Template Toolkit*. He is a regular speaker at Perl conferences
across Europe and often runs training courses alongside those conferences.

He runs Magnum Solutions Ltd., a London-based Perl consultancy and would be
happy to write Perl code for your company or train your programmers to
write better Perl code. See the
[Magnum Solutions web site](https://mag-sol.com/) for details.

You can also read his Perl blog, [Perl Hacks](https://perlhacks.com/).

Dave lives in Balham, South London with his wife. He runs various web
sites, blogs a bit and spends too many evenings watching live music.

He is [\@davorg](https://twitter.com/davorg) on Twitter.
