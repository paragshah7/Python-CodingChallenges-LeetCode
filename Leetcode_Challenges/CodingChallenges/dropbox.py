"""
textEditor1_2
(Task 1 of 1)
Submitted
0:08:40
Codewriting

Scenario
Your task is to implement a simplified version of text editor.

All operations that should be supported are listed below. Partial credit will be given for each implemented operation. Please submit often to ensure partial credits are captured.

Implementation tips

Implement operations and provided steps one by one, and not all together, keeping in mind that you will need to make refactors to support each additional step. In the first three levels you can assume that only one text document is modified.

Note

As a result, for every operation that potentially modifies the document (APPEND, BACKSPACE, PASTE, UNDO, and REDO), append the current state of the text after applying the operation, to the results.

Level 1
The editor starts with a blank text document, with the cursor at initial position 0.

1. APPEND <text> should append the inputted string text to the document starting from the current position of the cursor. After the operation, the cursor should be at the end of the added string.

queries = [
    ["APPEND", "Hey"],               | "" -> "Hey"
    ["APPEND", " there"],            | "Hey" -> "Hey there"
    ["APPEND", "!"]                  | "Hey there" -> "Hey there!"
]

// returns: "Hey there!"
2. MOVE <position> should move the cursor to the specified position. The cursor should be positioned between document characters, and are enumerated sequentially starting from 0. If the specified position is out of bounds, then move the cursor to the nearest available position.

queries = [
    ["APPEND", "Hey you"],           | "" -> "Hey you"
    ["MOVE", "3"],                   | moves the cursor after the first "y"
    ["APPEND", ","]                  | "Hey you" -> "Hey, you"
]

// returns: "Hey, you"
3. BACKSPACE should remove the character right before the cursor, if any.

queries = [
    [APPEND", "Hey you"],            | "" -> "Hey you"
    ["BACKSPACE"],                   | "Hey you" -> "Hey yo"
    ["BACKSPACE"]                    | "Hey yo" -> "Hey y"
]

// returns: "Hey y"
and

queries = [
    ["APPEND", "!"],                 | "" -> "!"
    ["BACKSPACE"],                   | "!" -> ""
    ["BACKSPACE"]                    | "" -> ""
]

// returns: ""
Level 2
Introduce methods to copy a part of the document text.

4. SELECT <left> <right> should select the text between the left and right cursor positions. Selection borders should be returned to the bounds of the document. If the selection is empty, it becomes a cursor position. Any modification operation replace the selected text and places the cursor at the end of the modified segment.

For example, the following operations

queries = [
    ["APPEND", "Hello cruel world!"],  | "" -> "Hello cruel world!"
    ["SELECT", "5", "11"],             | selects " cruel"
    ["APPEND", ","]                    | "Hello cruel world!" -> "Hello, world!"
produce "Hello, world!" with the cursor positioned after the comma.

SELECT and APPEND should replace the selected characters with the appended characters:

queries = [
    ["APPEND", "Hello"],               | "" -> "Hello"
    ["SELECT", "2", "5"],              | Selects a substring "llo"
    ["APPEND", "y there"]              | "Hello" -> "Hey there"
]

// returns: "Hey there"
5. COPY should copy the selected text to the clipboard, if there is an active non-empty selection.
6. PASTE should append the text from the clipboard.

For example, the following operations

queries = [
    ["APPEND", "Hello, world!"],       | "" -> "Hello, world!"
    ["SELECT", "5", "12"],             | selects ", world"
    ["COPY"],                          | copies ", world"
    ["MOVE", "12"],                    | moves the cursor to after "d"
    ["PASTE"],                         | "Hello, world!" -> "Hello, world, world!"
    ["PASTE"]                          | "Hello, world, world!" -> "Hello, world, world, world!"
]
produce "Hello, world, world, world!".

Level 3
The text editor should allow document changes to be tracked and reverted. Consider only operations that actually modify the contents of the text document.

7. UNDO should restore the document to the state before the previous modification or REDO operation. The selection and cursor position should be also restored.

For example,

queries = [
    ["APPEND", "Hello, world!"],       | "" -> "Hello, world!"
    ["SELECT", "7", "12"],             | selects "world"
    ["BACKSPACE"],                     | "Hello, world!" -> "Hello, !"
    ["UNDO"],                          | restores "Hello, world!" with "world" selected
    ["APPEND", "you"]                  | "Hello, world!" -> "Hello, you!"
]

// returns "Hello, you!"
8. REDO can only be performed if the document has not been modified since the last UNDO operation. REDO should restore the state before the previous UNDO operation, including the selection and cursor position. Multiple UNDO and REDO operations can be performed in a row.

For example,

queries = [
    ["APPEND", "Hello, world!"],       | "" -> "Hello, world!"
    ["SELECT", "7", "12"],             | selects "world"
    ["BACKSPACE"],                     | "Hello, world!" -> "Hello, !"
    ["MOVE", "6"],                     | moves the cursor to after the comma
    ["UNDO"],                          | restores "Hello, world!" with "world" selected
    ["UNDO"],                          | restores initial ""
    ["REDO"],                          | restores "Hello, world!" with "world" selected
    ["REDO"]                           | restores "Hello, !" with the cursor after the comma
]

// Returns "Hello, !"
Level 4
The text editor should support multiple text documents with a common clipboard.

9. CREATE <name> should create a blank text document name. If such a file already exists, ignore the operation. Modification history is stored individually for each document.
10. SWITCH <name> should switch the current document to name. If there is no such file, ignore the operation. When switching to a file, the position of the cursor and selection should return to the state in which they were left.

Implementation guarantee: all operations from the previous levels can only be performed when there is an active document.

For example,

queries = [
    ["CREATE", "document1"],       | creates document1
    ["CREATE", "document2"],       | creates document2
    ["CREATE", "document1"],       | ignores the operation
    ["SWITCH", "document1"],       | switches to document1
    ["APPEND", "Hello, world!"],   | document1: "" -> "Hello, world!"
    ["SELECT", "7", "12"],         | selects "world"
    ["COPY"],                      | copies "world" to the clipboard
    ["SWITCH", "document2"],       | switches to document2
    ["PASTE"],                     | document2: "" -> "world"
    ["SWITCH", "document1"],       | switches to document1
    ["BACKSPACE"]                  | document1: "Hello, world!" -> "Hello, !"
]

// Returns "Hello, !"
Example

For
queries = [
    ["APPEND", "Hey"],
    ["APPEND", " you"],
    ["APPEND", ", don't"],
    ["APPEND", " "],
    ["APPEND", "let me down"]
]
the output should be

textEditor1_2(queries) = [
    "Hey",
    "Hey you",
    "Hey you, don't",
    "Hey you, don't ",
    "Hey you, don't let me down"
]
For
queries = [
    ["APPEND", "Hey, you!"],
    ["BACKSPACE"],
    ["APPEND", "? Impossibel!"],
    ["BACKSPACE"],
    ["BACKSPACE"],
    ["BACKSPACE"],
    ["APPEND", "le!"]
]
the output should be

textEditor1_2(queries) = [
    "Hey, you!",
    "Hey, you",
    "Hey, you? Impossibel!",
    "Hey, you? Impossibel",
    "Hey, you? Impossibe",
    "Hey, you? Impossib",
    "Hey, you? Impossible!"
]
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.string queries

An array of operations need to be applied to the text editor. It is guaranteed that each operation is one of the operations described in the description, all operation parameters are given in correct format, and the text editor will never be in an incorrect state that is not described in the description.

Guaranteed constraints:
1 ≤ queries.length ≤ 250.

[output] array.string

For every operation that modifies the text (APPEND, BACKSPACE, PASTE, UNDO, and REDO), append the current state of the text to the results.

[Python 3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name

Saved
383940414243444546473736353433
                print(prev_str)
                output_list.append(prev_str)
                move = l
                print(move)

            elif query[0] == 'BACKSPACE':
                if move == None:
                    # new_a = prev_str[:move-1]
                    # new_b = prev_str[move:]
                    # prev_str = new_a + new_b


TESTS
CUSTOM TESTS
Tests passed: 12/40.
Test 1
Test 2
Test 3
Test 4
Test 5
Test 6
Test 7
Test 8
Test 9
Test 10
Test 11
Test 12
Input:
queries:
[["APPEND","You'll never find a rainbow if you're looking down"],
 ["SELECT","0","27"],
 ["BACKSPACE"],
 ["SELECT","7","12"],
 ["APPEND","--replaced--"]]
Output:
["You'll never find a rainbow if you're looking down",
 " if you're looking down",
 " if you're looking down",
 " if youooking down"]
Expected Output:
["You'll never find a rainbow if you're looking down",
 " if you're looking down",
 " if you--replaced--ooking down"]
Console Output:
Parag
0 27
 if you're looking down
0
0
7 12
 if youooking down
7
Error Output:
Empty
Test 13
Test 14
Test 15
Test 16
Test 17
Test 18
Test 19
Test 20
Test 21
Test 22
Test 23
Test 24
Test 25
Test 26
Test 27
Test 28
Test 29
Test 30
Test 31
Test 32
Test 33
Test 34
Test 35
Test 36
Test 37
Test 38
Test 39
Test 40
MORE
300/1000
move
"""

def textEditor1_2(queries):
    output_list = []
    prev_str = ""
    prev_str_l = []
    # print(queries)
    str_p = 'Parag'
    print(str_p)

    move = None
    l = None
    sel_s = None

    for query in queries:
        # print(query)
        if l and query[0] == 'BACKSPACE':
            output_list.append(prev_str)
            l = None
            continue
        try:
            if query[0] == 'APPEND':
                if move == None:
                    prev_str = prev_str + query[1]
                elif move == 0:
                    prev_str = query[1] + prev_str
                elif move < 0:
                    prev_str = query[1] + prev_str
                elif move > 0:
                    new_a = prev_str[:move]
                    new_b = prev_str[move:]
                    print(new_a, new_b)
                    prev_str = new_a + query[1] + new_b
                    move += len(query[1])

                output_list.append(prev_str)

            elif query[0] == 'SELECT':
                l = int(query[1])
                r = int(query[2])
                new_a = prev_str[:l]
                new_b = prev_str[r:]
                prev_str = new_a + new_b
                sel_s = prev_str[l:r]
                print(l,r)
                print(prev_str)
                move = l
                print('move= ',move)

            elif query[0] == 'BACKSPACE':
                if move == None:
                    # new_a = prev_str[:move-1]
                    # new_b = prev_str[move:]
                    # prev_str = new_a + new_b
                    prev_str = prev_str[:-1]
                elif move > 0:
                    new_a = prev_str[:move-1]
                    new_b = prev_str[move:]
                    prev_str = new_a + new_b
                    move -= 1
                print(move)
                output_list.append(prev_str)
            elif query[0] == 'MOVE':
                move = int(query[1])
                print(move)
            else:
                continue
        except:
            continue
    # print(output_list)
    return output_list
