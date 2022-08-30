import wombat.io

FILENAME = 'capybaras.txt'

def test_inputstream(fs):
    with open(FILENAME, 'w') as f:
        f.write('Capybaras\n')

    stream = wombat.io.InputStream(FILENAME)
    assert stream.read()=='Capybaras\n'
