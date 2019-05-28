import math
import numpy


def encryptText(textToEncrypt,encryptSquare):
    row = math.ceil(math.sqrt(len(encryptSquare)))

    j = 0
    w = 0
    i = 0

    pRowIndex = 0
    pColumnIndex = 0
    qRowIndex = 0
    qColumnIndex = 0

    squareEncrypter = [[0 for x in range(row)] for y in range(row)]

    result = ""

    for x in range(len(encryptSquare)):
        if ((i == (row * j))):
            j = j + 1
            w = 0
        else:
            squareEncrypter[j - 1][w] = encryptSquare[i]
            w = w + 1
            i = i + 1

    lenghtResultText = 1

    while lenghtResultText < len(textToEncrypt):

        p = textToEncrypt[lenghtResultText - 1]
        q = textToEncrypt[lenghtResultText]

        for z in range(row):
            for x in range(row):
                if (squareEncrypter[z][x] == p):
                    pRowIndex = z
                    pColumnIndex = x
                if (squareEncrypter[z][x] == q):
                    qRowIndex = z
                    qColumnIndex = x

        if ((pColumnIndex == qColumnIndex) and (p != q)):
            if ((qRowIndex + 1) >= row or (pRowIndex + 1) >= row):
                result += squareEncrypter[0][pColumnIndex]
                result += squareEncrypter[0][qColumnIndex]
            else:
                result += squareEncrypter[pRowIndex + 1][pColumnIndex]
                result += squareEncrypter[qRowIndex + 1][qColumnIndex]

        elif ((pRowIndex == qRowIndex) and (p != q)):
            if ((qColumnIndex + 1) >= row or (pColumnIndex + 1) >= row):
                result += squareEncrypter[pRowIndex][0]
                result += squareEncrypter[qRowIndex][0]
            else:
                result += squareEncrypter[pRowIndex][pColumnIndex + 1]
                result += squareEncrypter[qRowIndex][qColumnIndex + 1]
        elif (p == q):
            result += p
            result += 'X'
            result += q
        else:
            result += squareEncrypter[qRowIndex][pColumnIndex]
            result += squareEncrypter[pRowIndex][qColumnIndex]

        lenghtResultText += 2

    return result