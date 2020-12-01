from sleeptrack import *

def test_date_to_dict():
    print('date to dict')
    assert date_to_dict('1998-11-25') == {'year': 1998, 'month': 11, 'day': 25}, date_to_dict('1998-11-25')
    assert date_to_dict('2001-09-16') == {'year': 2001, 'month': 9, 'day': 16}, date_to_dict('2001-09-16')

def test_check():
    print('check')
    assert check('sleeptrack.py', 'Sun') == True, check('sleeptrack.py', 'Sun')
    assert check('sleeptrack.py', 'Sat')  == True, check('sleeptrack.py', 'Sat')
    assert check('sleeptrack.py', 'Fat')  == False, check('sleeptrack.py', 'Fat')

def test_get_filesize():
    print('get filesize')
    assert get_filesize('test_delete.txt') == 27, get_filesize('test_delete.txt')
    assert get_filesize('test_graph.txt') == 29, get_filesize('test_graph.txt')
    assert get_filesize('test_rec.txt') == 19, get_filesize('test_rec.txt')

def test_emotion():
    print('emotion')
    assert emotion(1, markov) in '12', emotion(1, markov)
    assert emotion(2, markov) in '123', emotion(2, markov)
    assert emotion(3, markov) in '123', emotion(3, markov)
    assert emotion(4, markov) in '1234', emotion(4, markov)
    assert emotion(5, markov) in '12345', emotion(5, markov)
    assert emotion(6, markov) in '2345', emotion(6, markov)
    assert emotion(7, markov) in '2345', emotion(7, markov)
    assert emotion(8, markov) in '345', emotion(8, markov)
    assert emotion(9, markov) in '345', emotion(9, markov)
    assert emotion(10, markov) in '345', emotion(10, markov)

if __name__ == "__main__":
    test_date_to_dict()
    test_check()
    test_get_filesize()
    test_emotion()