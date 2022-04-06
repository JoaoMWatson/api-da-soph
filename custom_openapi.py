from fastapi.openapi.utils import get_openapi


def custom_openapi(app):
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title='Api de produtos',
        version='0.1.0',
        description='Essa api de produtos é daora d+',
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema
