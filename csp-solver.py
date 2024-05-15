def solve_CSP(input_dict):
    # YOUR CODE HERE. Do not change the name of the function
    """initializes csp from inout_dict and starts the backtracking algorithm"""
    csp = {"domains": input_dict["domains"], "constraints": input_dict["constraints"]}
    return backtracking(csp)
def backtracking(csp):
    """initializes an empty dictionary and starts recursive backtracking process"""
    assignment = {}
    return backtrack(assignment, csp)
def backtrack(assignment, csp):
    """this is the main recursive backtracking function. it assigns values to variables and backtracks when necessary"""
    # return a solution after checking if an assignment is complete
    if is_complete(assignment, csp):
        return assignment
    
    # select an unassigned variable to try next
    var = select_unassigned_variable(assignment, csp)
    # loop through all values in domain of selected variable
    for value in csp["domains"][var]:
        # assign a value to the variable and apply forward checking to prune domains
        assignment[var] = value
        domains = forward_checking(csp, var, value, assignment)
            
        # call backtrack with the new assignment for the variable
        if domains is not None:
            result = backtrack(assignment, csp)
            # return the solution if found
            if result is not None:
                return result
            
            # if no solution is found, then go back to the domains that were pruned
            for variable, domain in domains.items():
                csp["domains"][variable] = domain
        
        # get rid of the current assignment for the variable and try the next value
        del assignment[var]
    # no solution is found for the current path, so return None
    return None
    
def forward_checking(csp, var, value, assignment):
    """this function applies forward checking to prune domains of neighboring variables based on constraints"""
    original_domain = {}
    # loop through all constraints to find neighbors of the current variable
    for (str1, str2), constraint in csp["constraints"].items():
        if var == str1 or var == str2:
            neighbor = str2 if var == str1 else str1
            
            if neighbor not in assignment: # only consider neighbors that were not assigned yet
                original_domain[neighbor] = csp["domains"][neighbor]
                # prune neighbor's domain based on current assignment and constraints
                new_domain = [v for v in csp["domains"][neighbor] if (var == str1 and constraint(value, v)) or (var == str2 and constraint(v, value))]
                
                if not new_domain:
                    # restore original domains and return none
                    for n, domain in original_domain.items():
                        csp["domains"][n] = domain
                    return None
                
                # update neighbor's domain
                csp["domains"][neighbor] = new_domain
    
    # return original domain to restore
    return original_domain
    
def is_complete(assignment, csp):
    """checks if current assignment is complete by checking if all variables are assigned"""
    if set(assignment.keys()) == set(csp["domains"].keys()):
        return True
    return False
def select_unassigned_variable(assignment, csp):
    """selects an unassigned variable"""
    var = None
    size = float('inf')
    for variable, values in csp["domains"].items():
        if variable not in assignment:
            domain_size = len(values)
                    
            # use variables with a smaller domain to reduce search space
            if domain_size < size:
                size = domain_size
                var = variable
            
    return var
def order_domain_values(var, assignment, csp):
    """order values of a variables domain based on LCV heuristic"""
    # return if there is only one value
    if len(csp["domains"][var]) == 1:
        return csp["domains"][var]
        
    constraints_count_per_value = []
    for value in csp["domains"][var]:
        count = 0
        for (str1, str2), constraint in csp["constraints"].items():
            neighbor = None
            if var == str1:
                neighbor = str2
            
            if var == str2:
                neighbor = str1
            
            # only consider unassigned neighbors
            if neighbor is not None and neighbor not in assignment:
                for v in csp["domains"][neighbor]:
                    potential = assignment.copy()
                    potential[var] = value
                    # increase count of neighbor's domain if constrained
                    if not is_consistent(neighbor, v, potential, csp):
                        count += 1
                        
        constraints_count_per_value.append((value, count))
    
    # order values based on how few constraints they put on domains of neighbors
    sorted_values = [v for v, _ in sorted(constraints_count_per_value, key=lambda x: x[1])]
        
    return sorted_values
def is_consistent(var, value, assignment, csp):
    """check if a variable is consistent with constraints after assigning it a value"""
    # loop through keys and values in constraints
    for (str1, str2), constraint in csp["constraints"].items():
        # violates a constraint
        if var == str1 and str2 in assignment and not constraint(value, assignment[str2]):
            return False
                
        # violates a constraint
        if var == str2 and str1 in assignment and not constraint(assignment[str1], value):
                return False
    
    # does not violate a constraint
    return True