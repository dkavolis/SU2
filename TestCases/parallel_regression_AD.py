#!/usr/bin/env python

## \file parallel_regression.py
#  \brief Python script for automated regression testing of SU2 examples
#  \author A. Aranake, A. Campos, T. Economon, T. Lukaczyk, S. Padron
#  \version 6.2.0 "Falcon"
#
# The current SU2 release has been coordinated by the
# SU2 International Developers Society <www.su2devsociety.org>
# with selected contributions from the open-source community.
#
# The main research teams contributing to the current release are:
#  - Prof. Juan J. Alonso's group at Stanford University.
#  - Prof. Piero Colonna's group at Delft University of Technology.
#  - Prof. Nicolas R. Gauger's group at Kaiserslautern University of Technology.
#  - Prof. Alberto Guardone's group at Polytechnic University of Milan.
#  - Prof. Rafael Palacios' group at Imperial College London.
#  - Prof. Vincent Terrapon's group at the University of Liege.
#  - Prof. Edwin van der Weide's group at the University of Twente.
#  - Lab. of New Concepts in Aeronautics at Tech. Institute of Aeronautics.
#
# Copyright 2012-2019, Francisco D. Palacios, Thomas D. Economon,
#                      Tim Albring, and the SU2 contributors.
#
# SU2 is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# SU2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with SU2. If not, see <http://www.gnu.org/licenses/>.

# make print(*args) function available in PY2.6+, does'nt work on PY < 2.6
from __future__ import print_function

import sys
from TestCase import TestCase    

def main():
    '''This program runs SU2 and ensures that the output matches specified values. 
       This will be used to do checks when code is pushed to github 
       to make sure nothing is broken. '''

    test_list = []

    #####################################
    ### Disc. adj. compressible Euler ###
    #####################################

    # Inviscid NACA0012
    discadj_naca0012           = TestCase('discadj_naca0012')
    discadj_naca0012.cfg_dir   = "cont_adj_euler/naca0012"
    discadj_naca0012.cfg_file  = "inv_NACA0012_discadj.cfg"
    discadj_naca0012.test_iter = 100
    discadj_naca0012.test_vals = [-3.606841, -9.035214, -0.000000, 0.005688] #last 4 columns
    discadj_naca0012.su2_exec  = "parallel_computation.py -f"
    discadj_naca0012.timeout   = 1600
    discadj_naca0012.tol       = 0.00001
    test_list.append(discadj_naca0012)
   
    # Inviscid Cylinder 3D (multiple markers)
    discadj_cylinder3D           = TestCase('discadj_cylinder3D')
    discadj_cylinder3D.cfg_dir   = "disc_adj_euler/cylinder3D"
    discadj_cylinder3D.cfg_file  = "inv_cylinder3D.cfg"
    discadj_cylinder3D.test_iter = 5
    discadj_cylinder3D.test_vals = [-3.719306, -4.038129, 0.000000, 0.000000] #last 4 columns
    discadj_cylinder3D.su2_exec  = "parallel_computation.py -f"
    discadj_cylinder3D.timeout   = 1600
    discadj_cylinder3D.tol       = 0.00001
    test_list.append(discadj_cylinder3D)

    # Arina nozzle 2D
    discadj_arina2k              = TestCase('discadj_arina2k')
    discadj_arina2k.cfg_dir      = "disc_adj_euler/arina2k"
    discadj_arina2k.cfg_file     = "Arina2KRS.cfg"
    discadj_arina2k.test_iter    = 20
    discadj_arina2k.test_vals    = [-0.747330, -0.782632, 326.910000, 0.000000] #last 4 columns
    discadj_arina2k.su2_exec     = "parallel_computation.py -f"
    discadj_arina2k.timeout      = 8400
    discadj_arina2k.tol          = 0.00001
    test_list.append(discadj_arina2k)
    
    ####################################
    ### Disc. adj. compressible RANS ###
    ####################################

    # Adjoint turbulent NACA0012 SA
    discadj_rans_naca0012_sa           = TestCase('discadj_rans_naca0012_sa')
    discadj_rans_naca0012_sa.cfg_dir   = "disc_adj_rans/naca0012"
    discadj_rans_naca0012_sa.cfg_file  = "turb_NACA0012_sa.cfg"
    discadj_rans_naca0012_sa.test_iter = 10
    discadj_rans_naca0012_sa.test_vals = [-1.751966, 0.485697, 0.183154, -0.000018] #last 4 columns
    discadj_rans_naca0012_sa.su2_exec  = "parallel_computation.py -f"
    discadj_rans_naca0012_sa.timeout   = 1600
    discadj_rans_naca0012_sa.tol       = 0.00001
    test_list.append(discadj_rans_naca0012_sa)

    # Adjoint turbulent NACA0012 SST
    discadj_rans_naca0012_sst           = TestCase('discadj_rans_naca0012_sst')
    discadj_rans_naca0012_sst.cfg_dir   = "disc_adj_rans/naca0012"
    discadj_rans_naca0012_sst.cfg_file  = "turb_NACA0012_sst.cfg"
    discadj_rans_naca0012_sst.test_iter = 10
    discadj_rans_naca0012_sst.test_vals = [-1.654042, -0.500944, 0.154703, -0.000022] #last 4 columns
    discadj_rans_naca0012_sst.su2_exec  = "parallel_computation.py -f"
    discadj_rans_naca0012_sst.timeout   = 1600
    discadj_rans_naca0012_sst.tol       = 0.00001
    test_list.append(discadj_rans_naca0012_sst)

    #######################################
    ### Disc. adj. incompressible Euler ###
    #######################################

    # Adjoint Incompressible Inviscid NACA0012
    discadj_incomp_NACA0012           = TestCase('discadj_incomp_NACA0012')
    discadj_incomp_NACA0012.cfg_dir   = "disc_adj_incomp_euler/naca0012"
    discadj_incomp_NACA0012.cfg_file  = "incomp_NACA0012_disc.cfg"
    discadj_incomp_NACA0012.test_iter = 20
    discadj_incomp_NACA0012.test_vals = [20.000000, -3.595580, -2.549720, 0.000000] #last 4 columns
    discadj_incomp_NACA0012.su2_exec  = "parallel_computation.py -f"
    discadj_incomp_NACA0012.timeout   = 1600
    discadj_incomp_NACA0012.tol       = 0.00001
    test_list.append(discadj_incomp_NACA0012)

    #####################################
    ### Disc. adj. incompressible N-S ###
    #####################################

    # Adjoint Incompressible Viscous Cylinder (Heated)
    discadj_incomp_cylinder           = TestCase('discadj_incomp_cylinder')
    discadj_incomp_cylinder.cfg_dir   = "disc_adj_incomp_navierstokes/cylinder"
    discadj_incomp_cylinder.cfg_file  = "heated_cylinder.cfg"
    discadj_incomp_cylinder.test_iter = 20
    discadj_incomp_cylinder.test_vals = [20.000000, -2.104640, -2.004547, 0.0000e+00] #last 4 columns
    discadj_incomp_cylinder.su2_exec  = "parallel_computation.py -f"
    discadj_incomp_cylinder.timeout   = 1600
    discadj_incomp_cylinder.tol       = 0.00001
    test_list.append(discadj_incomp_cylinder)

    ######################################
    ### Disc. adj. incompressible RANS ###
    ######################################

    # Adjoint Incompressible Turbulent NACA 0012 SA
    discadj_incomp_turb_NACA0012_sa           = TestCase('discadj_incomp_turb_NACA0012_sa')
    discadj_incomp_turb_NACA0012_sa.cfg_dir   = "disc_adj_incomp_rans/naca0012"
    discadj_incomp_turb_NACA0012_sa.cfg_file  = "turb_naca0012_sa.cfg"
    discadj_incomp_turb_NACA0012_sa.test_iter = 10
    discadj_incomp_turb_NACA0012_sa.test_vals = [10.000000, -3.846036, -1.031071, 0.000000] #last 4 columns
    discadj_incomp_turb_NACA0012_sa.su2_exec  = "parallel_computation.py -f"
    discadj_incomp_turb_NACA0012_sa.timeout   = 1600
    discadj_incomp_turb_NACA0012_sa.tol       = 0.00001
    test_list.append(discadj_incomp_turb_NACA0012_sa)

    # Adjoint Incompressible Turbulent NACA 0012 SST
    discadj_incomp_turb_NACA0012_sst           = TestCase('discadj_incomp_turb_NACA0012_sst')
    discadj_incomp_turb_NACA0012_sst.cfg_dir   = "disc_adj_incomp_rans/naca0012"
    discadj_incomp_turb_NACA0012_sst.cfg_file  = "turb_naca0012_sst.cfg"
    discadj_incomp_turb_NACA0012_sst.test_iter = 10
    discadj_incomp_turb_NACA0012_sst.test_vals = [-3.845805, -2.415680, -8.430441, 0.000000] #last 4 columns
    discadj_incomp_turb_NACA0012_sst.su2_exec  = "parallel_computation.py -f"
    discadj_incomp_turb_NACA0012_sst.timeout   = 1600
    discadj_incomp_turb_NACA0012_sst.tol       = 0.00001
    test_list.append(discadj_incomp_turb_NACA0012_sst)

    #######################################################
    ### Unsteady Disc. adj. compressible RANS           ###
    #######################################################
   
    # Turbulent Cylinder
    discadj_cylinder           = TestCase('unsteady_cylinder')
    discadj_cylinder.cfg_dir   = "disc_adj_rans/cylinder"
    discadj_cylinder.cfg_file  = "cylinder.cfg" 
    discadj_cylinder.test_iter = 9
    discadj_cylinder.test_vals = [3.746900, -1.544893, -8.3447e-03, 1.3808e-05] #last 4 columns
    discadj_cylinder.su2_exec  = "parallel_computation.py -f"
    discadj_cylinder.timeout   = 1600
    discadj_cylinder.tol       = 0.00001
    discadj_cylinder.unsteady  = True
    test_list.append(discadj_cylinder)

    ##########################################################################
    ### Unsteady Disc. adj. compressible RANS DualTimeStepping 1st order   ###
    ##########################################################################

    # Turbulent Cylinder
    discadj_DT_1ST_cylinder           = TestCase('unsteady_cylinder_DT_1ST')
    discadj_DT_1ST_cylinder.cfg_dir   = "disc_adj_rans/cylinder_DT_1ST"
    discadj_DT_1ST_cylinder.cfg_file  = "cylinder.cfg"
    discadj_DT_1ST_cylinder.test_iter = 9
    discadj_DT_1ST_cylinder.test_vals = [3.698165, -1.607052, -2.2503e-03, 2.7212e-05] #last 4 columns
    discadj_DT_1ST_cylinder.su2_exec  = "parallel_computation.py -f"
    discadj_DT_1ST_cylinder.timeout   = 1600
    discadj_DT_1ST_cylinder.tol       = 0.00001
    discadj_DT_1ST_cylinder.unsteady  = True
    test_list.append(discadj_DT_1ST_cylinder)

    #######################################################
    ### Disc. adj. turbomachinery                       ###
    #######################################################
    
    # Transonic Stator 2D
    discadj_trans_stator           = TestCase('transonic_stator')
    discadj_trans_stator.cfg_dir   = "disc_adj_turbomachinery/transonic_stator_2D"
    discadj_trans_stator.cfg_file  = "transonic_stator.cfg" 
    discadj_trans_stator.test_iter = 79
    discadj_trans_stator.test_vals = [79.000000,-1.923936, -2.119783] #last 4 columns
    discadj_trans_stator.su2_exec  = "parallel_computation.py -f"
    discadj_trans_stator.timeout   = 1600
    discadj_trans_stator.tol       = 0.00001
    test_list.append(discadj_trans_stator)
    
    ###################################
    ### Structural Adjoint          ###
    ###################################
   
    # Structural model
    discadj_fea           = TestCase('discadj_fea')
    discadj_fea.cfg_dir   = "disc_adj_fea"
    discadj_fea.cfg_file  = "configAD_fem.cfg" 
    discadj_fea.test_iter = 9
    discadj_fea.test_vals = [-5.394766, -5.572142, -0.000364, -8.708681] #last 4 columns
    discadj_fea.su2_exec  = "parallel_computation.py -f"
    discadj_fea.timeout   = 1600
    discadj_fea.tol       = 0.00001
    test_list.append(discadj_fea) 

    ###################################
    ### Disc. adj. heat             ###
    ###################################

    # Discrete adjoint for heated cylinder
    discadj_heat           = TestCase('discadj_heat')
    discadj_heat.cfg_dir   = "disc_adj_heat"
    discadj_heat.cfg_file  = "disc_adj_heat.cfg"
    discadj_heat.test_iter = 10
    discadj_heat.test_vals = [3.183906, 0.923840, -223.200000, -2059.800000] #last 4 columns
    discadj_heat.su2_exec  = "parallel_computation.py -f"
    discadj_heat.timeout   = 1600
    discadj_heat.tol       = 0.00001
    test_list.append(discadj_heat)

    ###################################
    ### Coupled FSI Adjoint         ###
    ###################################
   
#    # Structural model
#    discadj_fsi           = TestCase('discadj_fsi')
#    discadj_fsi.cfg_dir   = "disc_adj_fsi"
#    discadj_fsi.cfg_file  = "configAD_fsi.cfg" 
#    discadj_fsi.test_iter = 3000
#    discadj_fsi.test_vals = [0.958848,-0.157183,0.658415,1.302076] #last 4 columns
#    discadj_fsi.su2_exec  = "parallel_computation.py -f"
#    discadj_fsi.timeout   = 1600
#    discadj_fsi.tol       = 0.00001
#    test_list.append(discadj_fsi)

    ###################################
    ### Coupled CHT Adjoint         ###
    ###################################

    # Coupled discrete adjoint for heatflux in heated cylinder array
    discadj_cht           = TestCase('discadj_cht')
    discadj_cht.cfg_dir   = "coupled_cht/disc_adj_incomp_2d"
    discadj_cht.cfg_file  = "cht_2d_3cylinders.cfg"
    discadj_cht.test_iter = 10
    discadj_cht.test_vals = [-2.406699, -3.097572, -3.097543, -3.095282] #last 4 columns
    discadj_cht.su2_exec  = "parallel_computation.py -f"
    discadj_cht.timeout   = 1600
    discadj_cht.tol       = 0.00001
    test_list.append(discadj_cht)		

    ######################################
    ### RUN TESTS                      ###
    ######################################

    pass_list = [ test.run_test() for test in test_list ]

    ##################################################
    ### Structural Adjoint - Topology Optimization ###
    ##################################################

    # test discrete_adjoint.py
    discadj_topol_optim = TestCase('discadj_topol_optim')
    discadj_topol_optim.cfg_dir = "fea_topology"
    discadj_topol_optim.cfg_file  = "config.cfg"
    discadj_topol_optim.test_iter = 0
    discadj_topol_optim.su2_exec  = "parallel_computation.py"
    discadj_topol_optim.timeout   = 1600
    discadj_topol_optim.reference_file = "grad_ref_node.dat.ref"
    discadj_topol_optim.test_file = "grad_ref_node.dat"
    pass_list.append(discadj_topol_optim.run_filediff())
    test_list.append(discadj_topol_optim)

    ###################################
    ### Coupled FSI Adjoint         ###
    ###################################

#    discadj_fsi2           = TestCase('discadj_fsi_airfoil')
#    discadj_fsi2.cfg_dir   = "disc_adj_fsi/Airfoil_2d"
#    discadj_fsi2.cfg_file  = "config.cfg"
#    discadj_fsi2.test_iter = 0
#    discadj_fsi2.su2_exec  = "parallel_computation.py"
#    discadj_fsi2.timeout   = 1600
#    discadj_fsi2.reference_file = "grad_young.opt.ref"
#    discadj_fsi2.test_file = "grad_young.opt"
#    pass_list.append(discadj_fsi2.run_filediff())
#    test_list.append(discadj_fsi2)

    # Tests summary
    print('==================================================================')
    print('Summary of the parallel tests')
    print('python version:', sys.version)
    for i, test in enumerate(test_list):
        if (pass_list[i]):
            print('  passed - %s'%test.tag)
        else:
            print('* FAILED - %s'%test.tag)

    if all(pass_list):
        sys.exit(0)
    else:
        sys.exit(1)
    # done

if __name__ == '__main__':
    main()
