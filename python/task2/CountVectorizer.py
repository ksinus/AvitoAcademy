class CountVectorizer:
    def __init__(self):
        self._vocabulary = []

    def fit_transform(self, corpus):
        """Transform a sequence of documents to a document-term matrix.

        Parameters
        ----------
        corpus : iterable over raw text documents, length = n_samples

        Returns
        -------
        term_matrix : sparse matrix of shape (n_samples, n_features)
                      Document-term matrix.
        """
        self._init_vocabulary(corpus)
        term_matrix = [[]] * len(corpus)
        for i, token in enumerate(corpus):
            list_term = [term.lower() for term in token.split()]
            term_matrix[i] = [list_term.count(term)
                              for term in self._vocabulary]
        return term_matrix

    def get_feature_names(self):
        """Array mapping from feature integer indices to feature name.

        Returns
        -------
        feature_names : list
                        A list of feature names.
        """
        return self._vocabulary

    def _init_vocabulary(self, corpus):
        """Build a vocabulary of terms.

        Parameters
        ----------
        corpus : iterable over raw text documents, length = n_samples
        """
        self._vocabulary = list({term.lower()
                                 for token in corpus
                                 for term in token.split()})
