from fabric.colors import green
from fabric.decorators import task
from fabric.operations import local


@task
def test():
    """
    Run tests, make coverage reports, produce junit style test report
    """
    cmd = (
        './manage.py test '
        '--settings core.settings.tests '
    )

    print(green('\nRunning test suite\n'))
    local(cmd)
