'''
    Test suite for testing my implementations of all histograms
'''
import distogram
import listogram
import tistogram
import cistogram

def test_dictogram():
    '''
        Function for testing dictionary based histograms
    '''
    histogram = distogram.histogram('Hi there Hi bye hi hello bye bye bye hello', is_file=False)

    print(histogram)
    print(distogram.unique_words(histogram))
    print(distogram.frequency(histogram, 'HI'))

def test_listogram():
    '''
        Function for testing list based histograms
    '''
    histogram = listogram.histogram('Hi there Hi bye hi hello bye bye bye hello', is_file=False)

    print(histogram)
    print(listogram.unique_words(histogram))
    print(listogram.frequency(histogram, 'HI'))

def test_tistogram():
    '''
        Function for testing tuple based histograms
    '''
    histogram = tistogram.histogram('Hi there Hi bye hi hello bye bye bye hello', is_file=False)

    print(histogram)
    print(tistogram.unique_words(histogram))
    print(tistogram.frequency(histogram, 'HI'))

def test_cistogram():
    '''
        Function for testing count based histograms
    '''
    histogram = cistogram.histogram('Hi there there hi bye hi hello bye bye bye hello', is_file=False)

    print(histogram)
    print(cistogram.unique_words(histogram))
    print(tistogram.frequency(histogram, 'HI'))

if __name__ == '__main__':
    test_dictogram()
    test_listogram()
    test_tistogram()
    test_cistogram()
