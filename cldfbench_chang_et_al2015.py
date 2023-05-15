import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "chang_et_al2015"

    def cmd_makecldf(self, args):
        self.init(args)
        args.writer.add_summary(
            self.raw_dir.read_tree('mcc.trees', detranslate=True),
            self.metadata,
            args.log)

        args.writer.add_posterior(
            self.raw_dir.read_trees(
                'ieo.trees.gz',
                sample=1000,
                burnin=10001,
                detranslate=True),
            self.metadata,
            args.log,
            verbose=True)

        #args.writer.add_data(
        #    self.raw_dir.read_nexus('a1-c0-d0-g1-l2-s1-t1-z8_ieo.nex'),
        #    self.characters,
        #    args.log)
