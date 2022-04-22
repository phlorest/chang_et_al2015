import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "chang_et_al2015"

    def cmd_makecldf(self, args):
        self.init(args)
        
        summary = self.raw_dir.read_tree('mcc.trees', detranslate=True)
        args.writer.add_summary(summary, self.metadata, args.log)

        posterior = self.raw_dir.read_trees(
           'ieo.trees.gz',
           burnin=10001, sample=1000, detranslate=True)
        args.writer.add_posterior(posterior, self.metadata, args.log)
        
        args.writer.add_data(
            self.raw_dir.read_nexus('a1-c0-d0-g1-l2-s1-t1-z8_ieo.nex'),
            self.characters,
            args.log)
