# -*- coding: utf-8 -*-

"""
This module is used to:
1. use an html template pre-styled for a narrative/text div;
2. convert a bunch of mardown files in a given folder to html using above template;
3. save each output html file in ../frames/ for use by the sliderReport.
Command line call:
```
python -m prep_md2html
```
"""

def get_html_tpl(tpl_fullname):
    """ This uses FileSystemLoader (FSL), not PackageLoader.
        Assumes dir for FSL is tpl_fullname parent dir.
    """
    import os
    from jinja2 import Environment, FileSystemLoader
    
    tpl_dir = os.path.dirname(tpl_fullname)
    tpl_name = os.path.basename(tpl_fullname)
    
    jenv = Environment(loader=FileSystemLoader(tpl_dir), 
                       trim_blocks=True)
    return jenv.get_template(tpl_name)


def save_file(fname, ext, s, replace=True):
    """
    Usual write method of file handle used with
    json output if stream s is a dict.
    :param: fname: a file name
    :param: ext: output file extension
    :param: replace default (True):: overwrite
    """
    import os

   # check if fname has an extension:
    try:
        i = fname.index('.' , -6)
        outfile = fname[:i] + '.' + ext
    except:
        outfile = fname + '.' + ext
    
    if replace:
        if os.path.exists(outfile):
            os.remove(outfile)

    if isinstance(s, dict):
        import json

        with open(outfile, 'w') as f:
            f.write(json.dumps(s))
    else:
        if len(s):
            with open(outfile, 'w') as f:
                f.write(s)
    return


def embed_narratives(txt_dir, tpl_path, frame_dir):
    """
    To convert & save ./assets/txt/markdown narratives 
    to html in ./assets/frames/ using the html template
     ./assets/txt/narrative_template.html.
    """
    import os
    import glob
    import markdown

    html_tpl = get_html_tpl(tpl_path)
    
    g = glob.glob(os.path.join(txt_dir, '*.md'))

    for f in g:
        out = os.path.join(frame_dir,
                           'txt_' + 
                           os.path.basename(f)[:-3] + '.html')
        with markdown.codecs.open(f, encoding="utf-8") as md:
            html = markdown.markdown(md.read())
        html_out = html_tpl.render({'EMBED_TXT':html})
        save_file(out, 'html', html_out)


if __name__ == "__main__":
    import os

    assets_dir, _ = os.path.split(os.path.dirname(__file__))

    txt_dir = os.path.join(assets_dir, 'txt')
    tpl_path = os.path.join(txt_dir, 'narrative_template.html')
    frame_dir = os.path.join(assets_dir, 'frames')

    embed_narratives(txt_dir, tpl_path, frame_dir)
    