# The-Pur-Project-B

Remake of Pur, Pur originally was hard to develop

## How to install Pur?

Not that complicated yet

## What is Pur?

Pur is an open-source programming language developed in Python.

It was originally made in 2024, but the newest is in 2025.

## Why Pur?

Pur has a simple syntax with small command names so you can type fast.

It is also versatile, as you can go in the code and add commands for your programs. (Tho I don't advise this, may break your installation.)

If you want, the releases can also let you run them in executable form. (soon)

## Documentation

`prt` - prints a var or a string.

`into` - inputs into a var.

`get` - gets an external functionlib to run when

`runlib` - is called.

`if=` - checks if var/str is equal to var/str. Outputs to var or runs code until

`end` - , which is a universal to Pur end, for loops and conditionals.

`frvr` - Forever loop, uses `end` only for 'go to start again'

`runpy` - Runs a Python program, in your Pur program.

`uselib` - Uses a folder with Pur programs as a library. Classes are folders, methods are files.

### Syntax

Syntax is like this:

`command(input`

For each of what might be a period in the original Pur, is now a left circle bracket.

### Built-in libraries

Breakfast - function library to ensure Pur is working properly by saying foods - used for debugging the user modified Pur, or me, to test stuff.

Quiz - program library. Sample proglib to show you the power of Pur 1.2.

rlib - regular library. It means 'repeating libs'. Made for `uselib`.

### How to use the interpreter after you make your code?

Luckily, Pur is easy, so the arguments are tiny!

To run a file using the Pur interpreter, do `python3 main.py your_program`.

### How do I make a library?

- Although you can't publish one yet, you can transfer it around.

To make a library, you need to make a folder.

After that, making functions is easy. You can't give input yet, but to make one, go into the folder, and create a Pur program.

### How do I use a library?

Really simple to do that.

First, you (ofc) make a program doing stuff.

When you want to use a library,

you call the `get` command and for the input, do the directory of the library.

After that, you call `uselib` with two inputs. The first one is the directory of it.

The second input is the last one, soon to be only 2 or 3 inputs. It is the filename of the function.

## Examples

Forever - forever loop!

```
prt(Starting Forever...
frvr(
prt(FOREVER!
end(
```
