from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('kotti_blogtool')


def kotti_configure(settings):
    settings['pyramid.includes'] += ' kotti_blogtool.views'
    settings['kotti.available_types'] +=\
        ' kotti_blogtool.resources.Blog kotti_blogtool.resources.BlogEntry'
    settings['kotti.populators'] += ' kotti_blogtool.populate.populate_settings'


def includeme(config):

    config.add_translation_dirs('kotti_blogtool:locale')
    config.scan(__name__)
