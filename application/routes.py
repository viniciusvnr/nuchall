from  flask import jsonify, request
import json

api_version = '/api/v0.1'


def get_version():
    return 'nuchall - Beta API - v0.1'


def init_api_routes(app):
    if app:
        app.add_url_rule('/api', 'version', get_version, methods=['GET'])
        app.add_url_rule(api_version + '/routes', 'list_routes', list_routes, methods=['GET'], defaults={'app': app})
        # app.add_url_rule(api_version + '/account', 'account')


def list_routes(app):
    result = []
    for rt in app.url_map.iter_rules():
        result.append({
            'methods': list(rt.methods),
            'route': str(rt)
        })
    return jsonify({
        'route': result,
        'total': len(result)
    })
