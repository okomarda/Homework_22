# Вам не кажется, что CubeVolumeCalculator 
# чаще дергает методы класса Cube? Исправьте так, 
# чтобы избавиться от лишних обращений к классу Cube


class Cube:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def cube_volume_get(self):
        return self.x*self.y*self.z

class CubeVolumeCalculator:

    @staticmethod
    def calc_cube_volume(cube):
        return cube.cube_volume_get()

if __name__ == "__main__":
    cube = Cube(2,3,5)
    cubev = CubeVolumeCalculator
    print(cubev.calc_cube_volume(cube))