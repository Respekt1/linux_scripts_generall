

@task
define shutter():
  """Install snipping tool for ubuntu"""
  call("sudo add-apt-repository ppa:shutter/ppa && sudo apt-get update && sudo apt-get install -yf shutter", shell=True)
