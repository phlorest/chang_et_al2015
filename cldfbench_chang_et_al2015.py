import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "chang_et_al2015"

    def cmd_makecldf(self, args):
        self.init(args)
        args.writer.add_summary(
            self.raw_dir.joinpath('a1-c0-d0-g1-l2-s1-t1-z8').read_tree(
                'mcc.trees', detranslate=True),
            self.metadata,
            args.log)
        posterior = self.sample(
            self.remove_burnin(
                self.raw_dir.joinpath('analyses').read('ieo.trees.gz'),
                10001),
            detranslate=True,
            as_nexus=True)

        args.writer.add_posterior(
            posterior.trees.trees,
            self.metadata,
            args.log,
            verbose=True)
        args.writer.add_data(
            self.raw_dir.read_nexus('a1-c0-d0-g1-l2-s1-t1-z8_ieo.nex'),
            self.characters,
            args.log)
