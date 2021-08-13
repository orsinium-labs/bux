import subprocess
# import io
import sys


def test_version():
    cmd = [sys.executable, '-m', 'bux', 'version']
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    assert result.returncode == 0
    out = result.stdout.decode()
    assert out.count('.') == 2
    assert out[0].isdigit()
