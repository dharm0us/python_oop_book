# pickle, but you can't pickle things like timer/socket/connection etc
# so you have get_state and set_state to customize the pickle and unpickle process
# JSON doesn't have any support for executable code, unlike xml/yaml, so it's safer in that sense
