#9/10
import numpy as np

def str2num(string):
    total_val=0
    for i in string:
        total_val+=ord(i)-96
    return total_val

with open("puzzle9input.txt","r") as puzzle:
    puzzle = puzzle.read().replace('\n','')
##print(puzzle)
##puzzle='UfHhDmlLMhHdzZFzZuUuUuwWF'
letter='z'
puzzle=puzzle.replace(letter,'')
puzzle=puzzle.replace(letter.upper(),'')
found = False
while True:
    if 'aA' in puzzle:
        puzzle=puzzle.replace('aA','')
    elif 'Aa' in puzzle:
        puzzle=puzzle.replace('Aa','')
    elif 'bB' in puzzle:
        puzzle=puzzle.replace('bB','')
    elif 'Bb' in puzzle:
        puzzle=puzzle.replace('Bb','')
    elif 'cC' in puzzle:
        puzzle=puzzle.replace('cC','')
    elif 'Cc' in puzzle:
        puzzle=puzzle.replace('Cc','')
    elif 'dD' in puzzle:
        puzzle=puzzle.replace('dD','')
    elif 'Dd' in puzzle:
        puzzle=puzzle.replace('Dd','')
    elif 'eE' in puzzle:
        puzzle=puzzle.replace('eE','')
    elif 'Ee' in puzzle:
        puzzle=puzzle.replace('Ee','')
    elif 'fF' in puzzle:
        puzzle=puzzle.replace('fF','')
    elif 'Ff' in puzzle:
        puzzle=puzzle.replace('Ff','')
    elif 'gG' in puzzle:
        puzzle=puzzle.replace('gG','')
    elif 'Gg' in puzzle:
        puzzle=puzzle.replace('Gg','')
    elif 'hH' in puzzle:
        puzzle=puzzle.replace('hH','')
    elif 'Hh' in puzzle:
        puzzle=puzzle.replace('Hh','')
    elif 'iI' in puzzle:
        puzzle=puzzle.replace('iI','')
    elif 'Ii' in puzzle:
        puzzle=puzzle.replace('Ii','')
    elif 'jJ' in puzzle:
        puzzle=puzzle.replace('jJ','')
    elif 'Jj' in puzzle:
        puzzle=puzzle.replace('Jj','')
    elif 'kK' in puzzle:
        puzzle=puzzle.replace('kK','')
    elif 'Kk' in puzzle:
        puzzle=puzzle.replace('Kk','')
    elif 'lL' in puzzle:
        puzzle=puzzle.replace('lL','')
    elif 'Ll' in puzzle:
        puzzle=puzzle.replace('Ll','')
    elif 'mM' in puzzle:
        puzzle=puzzle.replace('mM','')
    elif 'Mm' in puzzle:
        puzzle=puzzle.replace('Mm','')
    elif 'nN' in puzzle:
        puzzle=puzzle.replace('nN','')
    elif 'Nn' in puzzle:
        puzzle=puzzle.replace('Nn','')
    elif 'oO' in puzzle:
        puzzle=puzzle.replace('oO','')
    elif 'Oo' in puzzle:
        puzzle=puzzle.replace('Oo','')
    elif 'pP' in puzzle:
        puzzle=puzzle.replace('pP','')
    elif 'Pp' in puzzle:
        puzzle=puzzle.replace('Pp','')
    elif 'qQ' in puzzle:
        puzzle=puzzle.replace('qQ','')
    elif 'Qq' in puzzle:
        puzzle=puzzle.replace('Qq','')
    elif 'rR' in puzzle:
        puzzle=puzzle.replace('rR','')
    elif 'Rr' in puzzle:
        puzzle=puzzle.replace('Rr','')
    elif 'sS' in puzzle:
        puzzle=puzzle.replace('sS','')
    elif 'Ss' in puzzle:
        puzzle=puzzle.replace('Ss','')
    elif 'tT' in puzzle:
        puzzle=puzzle.replace('tT','')
    elif 'Tt' in puzzle:
        puzzle=puzzle.replace('Tt','')
    elif 'uU' in puzzle:
        puzzle=puzzle.replace('uU','')
    elif 'Uu' in puzzle:
        puzzle=puzzle.replace('Uu','')
    elif 'vV' in puzzle:
        puzzle=puzzle.replace('vV','')
    elif 'Vv' in puzzle:
        puzzle=puzzle.replace('Vv','')
    elif 'wW' in puzzle:
        puzzle=puzzle.replace('wW','')
    elif 'Ww' in puzzle:
        puzzle=puzzle.replace('Ww','')
    elif 'xX' in puzzle:
        puzzle=puzzle.replace('xX','')
    elif 'Xx' in puzzle:
        puzzle=puzzle.replace('Xx','')
    elif 'yY' in puzzle:
        puzzle=puzzle.replace('yY','')
    elif 'Yy' in puzzle:
        puzzle=puzzle.replace('Yy','')
    elif 'zZ' in puzzle:
        puzzle=puzzle.replace('zZ','')
    elif 'Zz' in puzzle:
        puzzle=puzzle.replace('Zz','')
    else:
        break

print(letter, len(puzzle))



        
