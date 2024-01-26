from .tmux_launcher import Options, TmuxLauncher


class Launcher(TmuxLauncher):
    def common_options(self):
        return [
            # Command 0
            Options(
                dataroot="./datasets/single_object_200x100",
                name="gan_52",
                model="cycle_gan",
                crop_size=52,
                load_size=58,
            ),

            # Command 1
            Options(
                dataroot="./datasets/single_object_200x100",
                name="gan_76",
                model="cycle_gan",
                crop_size=76,
                load_size=85,
            ),

            # Command 2
            Options(
                dataroot="./datasets/single_object_200x100",
                name="gan_104",
                model="cycle_gan",
                crop_size=104,
                load_size=116,
            ),

            # Command 3
            Options(
                dataroot="./datasets/single_object_200x100",
                name="gan_128",
                model="cycle_gan",
                crop_size=128,
                load_size=143,
            ),

            # Command 4
            Options(
                dataroot="./datasets/single_object_200x100",
                name="gan_256",
                model="cycle_gan",
                crop_size=256,
                load_size=286,
            ),
        ]

    def commands(self):
        return ["python train.py " + str(opt) for opt in self.common_options()]

    def test_commands(self):
        # RussianBlue -> Grumpy Cats dataset does not have test split.
        # Therefore, let's set the test split to be the "train" set.
        return ["python test.py " + str(opt.set(phase='train')) for opt in self.common_options()]

# # Command 0
# Options(
#     dataroot="./datasets/single_object_200x100",
#     name="single_object_256_1",
#     CUT_mode="CUT"
# ),

# # Command 1
# Options(
#     dataroot="./datasets/single_object_200x100",
#     name="single_object_256_2",
#     CUT_mode="CUT",
# ),

# # Command 2
# Options(
#     dataroot="./datasets/single_object_200x100",
#     name="single_object_128_1",
#     CUT_mode="CUT",
#     crop_size=128,
#     load_size=144,
#     netF_nc=128,
#     num_patches=128,
# ),

# # Command 3
# Options(
#     dataroot="./datasets/single_object_200x100",
#     name="single_object_128_2",
#     CUT_mode="CUT",
#     crop_size=128,
#     load_size=144,
#     netF_nc=128,
#     num_patches=128,
# ),

# # Command 4
# Options(
#     dataroot="./datasets/single_object_200x100",
#     name="single_object_128_CG",
#     model="cycle_gan",
#     crop_size=128,
#     load_size=144,
# ),

# # Command 5
# Options(
#     dataroot="./datasets/single_object_200x100",
#     name="single_object_256_CG",
#     model="cycle_gan",
# ),