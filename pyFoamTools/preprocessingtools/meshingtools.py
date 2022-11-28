import sys,os
import yaml
import numpy as np
import pandas as pd
import stl

class geometry:
    def __init__(self,filename) -> None:
        self.my_stl = stl.mesh.Mesh.from_file(filename)

    def check_stl_is_closed(self):
        return self.my_stl.is_closed()