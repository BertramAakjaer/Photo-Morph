import itertools

class Pixel:
    def __init__(self, RGB, x, y):
        self.R = RGB[0]
        self.G = RGB[1]
        self.B = RGB[2]

        self.x = x
        self.y = y

class PixelGroups:
    def __init__(self, width, height, twoDiffence = 4):
        self.width = width
        self.height = height

        self.groups_pr_value = int(256 / (2 * twoDiffence))
        self.groups = self.init_list(self.groups_pr_value)

        self.sorted_merged_list = []
    
    def init_list(self, n, depth = 3):
        if depth == 0:
            return []
        return [self.init_list(n, depth - 1) for _ in range(n)]
    
    def add_pixel(self, RGB, x, y):
        r_index = RGB[0] // self.groups_pr_value
        g_index = RGB[1] // self.groups_pr_value
        b_index = RGB[2] // self.groups_pr_value

        self.groups[r_index][g_index][b_index].append(Pixel(RGB, x, y))

    def get_sorted_groups(self):
        flat_list = []
        
        for r_dim in self.groups:
            for g_dim in r_dim:
                for b_list in g_dim:
                    if b_list:
                        flat_list.append(b_list)

        sorted_list = sorted(flat_list, key=len)
        merged_list = list(itertools.chain.from_iterable(sorted_list))

        if (len(merged_list) == self.width * self.height):
            # print("To list function was succesfull !!")
            self.sorted_merged_list = merged_list
        else:
            #print("An error occurred !!")
            #print(f"list lenght: {len(merged_list)}")
            #print(f"Pixel count {self.width * self.height}")
            self.sorted_merged_list = []