import pathlib

from tqdm import tqdm
import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "chang_et_al2015"

    def cmd_makecldf(self, args):
        self.init(args)
        with self.nexus_summary() as nex:
            self.add_tree_from_nexus(
                args,
                self.raw_dir / 'a1-c0-d0-g1-l2-s1-t1-z8' / 'mcc.trees',
                nex,
                'summary',
                detranslate=True,
            )
        posterior = self.sample(
            self.remove_burnin(
                self.read_gzipped_text(self.raw_dir / 'analyses' / 'ieo.trees.gz'),
                10001),
            detranslate=True,
            as_nexus=True)

        with self.nexus_posterior() as nex:
            for i, tree in tqdm(enumerate(posterior.trees.trees, start=1), total=1000):
                self.add_tree(args, tree, nex, 'posterior-{}'.format(i))

        self.add_data(args, self.raw_dir / 'a1-c0-d0-g1-l2-s1-t1-z8_ieo.nex')
