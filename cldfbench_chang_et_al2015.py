import pathlib
import itertools
import collections

from commonnexus.blocks.characters import Characters
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

        # Add the semicolon terminating the MATRIX command:
        nex = self.raw_dir.read_nexus(
            'a1-c0-d0-g1-l2-s1-t1-z8_ieo.nex',
            preprocessor=lambda s: s.replace('end;', ';\nend;'))

        # Add meaningful character labels:
        charlabels = {}
        for label, sites in itertools.groupby(self.characters, lambda i: i['Label']):
            for i, site in enumerate(sites, start=1):
                charlabels[site['Site']] = '{}_{}'.format(label, i)
        matrix = collections.OrderedDict()
        for lid, vals in nex.characters.get_matrix().items():
            matrix[lid] = collections.OrderedDict(
                [(charlabels[site], val) for site, val in vals.items()])
        nex.replace_block(nex.DATA, Characters.from_data(matrix))

        args.writer.add_data(nex, self.characters, args.log)

