#-*-coding:utf-8-*-

import pystache
import json
import re


def render_template():
    template_file = open('template.html', 'r')
    json_conf_file = open('conf.json', 'r')

    try:
        json_dict = json.loads(json_conf_file.read())
        template = remove_lines_if_empty_json(template_file.read(), json_dict)
        result = pystache.render(template, json_dict)
    finally:
        template_file.close()
        json_conf_file.close()

    return result


def remove_lines_if_empty_json(template, json):
    if json['author'] == '':
        template = re.sub(r' *<meta name="author" content="\{\{author\}\}" />\n', '', template)

    if json['description'] == '':
        template = re.sub(r' *<meta name="description" content="\{\{description\}\}" />\n', '', template)

    if json['title'] == '':
        template = re.sub(r' *<title>\{\{title\}\}</title>\n', '', template)

    if json['css'] == '':
        template = re.sub(r' *<link rel="stylesheet" href="\{\{css\}\}" />\n', '', template)

    if json['favicon'] == '':
        template = re.sub(r' *<link rel="icon" href="\{\{favicon\}\}" />\n', '', template)

    if json['js'] == '':
        template = re.sub(r' *<script src="\{\{js\}\}"></script>\n', '', template)

    return template


def write_result(result):
    result_file = open('result.html', 'w')

    try:
        result_file.write(result)
    finally:
        result_file.close()


if __name__ == '__main__':
    write_result(render_template())
    print('Done.')
