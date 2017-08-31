c = get_config()
c.Exporter.preprocessors = [ 'bibpreprocessor.BibTexPreprocessor', 'pre_pymarkdown.PyMarkdownPreprocessor' ]
c.Exporter.template_file = 'revtex_nocode.tplx'