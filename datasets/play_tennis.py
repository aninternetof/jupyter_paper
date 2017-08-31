from sklearn.feature_extraction import DictVectorizer
from collections import namedtuple

class load_play_tennis:

    def __init__(self):
        Example = namedtuple('Example', ['inputs', 'label'])
        Input = namedtuple('Input', ['outlook', 'temperature', 'humidity', 'wind'])
        Label = namedtuple('Label', ['play_tennis'])

        examples = [
            Example(Input('sunny', 'hot', 'high', 'weak'), Label('no')),
            Example(Input('sunny', 'hot', 'high', 'strong'), Label('no')),
            Example(Input('overcast', 'hot', 'high', 'weak'), Label('yes')),
            Example(Input('rain', 'mild', 'high', 'weak'), Label('yes')),
            Example(Input('rain', 'cool', 'normal', 'weak'), Label('yes')),
            Example(Input('rain', 'cool', 'normal', 'strong'), Label('no')),
            Example(Input('overcast', 'cool', 'normal', 'strong'), Label('yes')),
            Example(Input('sunny', 'mild', 'high', 'weak'), Label('no')),
            Example(Input('sunny', 'cool', 'normal', 'weak'), Label('yes')),
            Example(Input('rain', 'mild', 'normal', 'weak'), Label('yes')),
            Example(Input('sunny', 'mild', 'normal', 'strong'), Label('yes')),
            Example(Input('overcast', 'mild', 'high', 'strong'), Label('yes')),
            Example(Input('overcast', 'hot', 'normal', 'weak'), Label('yes')),
            Example(Input('rain', 'mild', 'high', 'strong'), Label('no')),
        ]

        inputs = [example.inputs._asdict() for example in examples]
        labels = [example.label._asdict() for example in examples]

        input_vec = DictVectorizer()
        output_vec = DictVectorizer()

        # Use these
        self.data = input_vec.fit_transform(inputs).toarray()
        self.feature_names = input_vec.get_feature_names()
        self.target = output_vec.fit_transform(labels).toarray()
        self.target_names = [label for label in labels[0].items()]