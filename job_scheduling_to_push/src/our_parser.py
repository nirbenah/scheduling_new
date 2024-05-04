import argparse
from typing import List
from lin_prog_solver import *
from utils import *
from real_exact import *
from w_max_sat_reduction import *


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('input_problem', help='Instance file format, which specifies the jobs, the machines, and the time matrix specifying the run time of each job on each machine.', type = str)
    solution_type = parser.add_mutually_exclusive_group(required=True)
    solution_type.add_argument('-m', '--makespan', help='prints the makespan of the given schedule file. Should be activated with: schedule file format, which specifies an assignment of jobs to machines.', type = str)
    solution_type.add_argument('-a', '--approx', help='prints an approximate schedule by the approx solver', action='store_true')
    solution_type.add_argument('-ei', '--exact_ilp', help='prints a schedule by exact_ilp', action='store_true')
    solution_type.add_argument('-di', '--dump_ilp', help='prints the ILP program', action='store_true')
    solution_type.add_argument('-em', '--exact_maxsat', help='prints a scheudle by exact_maxsat', action = 'store_true')
    solution_type.add_argument('-dm', '--dump_maxsat', help='prints the MaxSat program', action = 'store_true')

    args = parser.parse_args()

    print(f"Working on file \"{args.input_problem}\"\n")
    matrix_from_input = read_file_to_list_of_lists(args.input_problem)
    original_p = transpose(matrix_from_input)
    if args.makespan:
        print(f"calculating the makespan of the schedule \'{args.makespan}\'....\n")
        sol_m_j = read_file_to_dict(args.makespan)
        #print(sol_m_j)
        print_run_time_of_machines(machine_with_times(add_times_to_m_j(sol_m_j, original_p)))
        
    if args.approx:
        print("calculating the approximate solution....\n")
        approx = ApproxSolver(original_p)
        print_dict(approx.machine_with_jobs_solution())
    if args.exact_ilp:
        print("calculating the exact_ilp solution....\n")
        exact_ilp = ExactILP(original_p)
        exact_ilp.job_and_machine_solution()
    if args.dump_ilp:
            print("calculating the MaxSat program....\n")
    if args.exact_maxsat:
        print("calculating the exact_maxsat solution....\n")
        exact_maxsat = MaxSatSolver(original_p)
        print(exact_maxsat.job_and_machine_solution())
    if args.dump_maxsat:
        print("calculating the dump_maxsat program....\n")
        dump_maxsat = MaxSatSolver(original_p)
        dump_maxsat.dump_maxsat()

    print("BYE")


if __name__ == '__main__':
    exit(main())
