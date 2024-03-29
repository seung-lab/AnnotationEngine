class AnnotationEngineException(Exception):
    """ generic error in annotation engine """

    pass


class UnknownAnnotationTypeException(Exception):
    """ error raised when an annotation type is not found """

    pass


class AnnotationNotFoundException(AnnotationEngineException):
    """ error raised when an annotation is not found """

    pass


class AlignedVolumeNotFoundException(AnnotationEngineException):
    """ error raised when a aligned_volume is not found """


class SchemaServiceError(AnnotationEngineException):
    """ error raised when schema can't be loading from schema service """
