# Legal Tech Assistant - Demo Script

## 🎯 Demo Overview
This script demonstrates all features of the Legal Tech Assistant application, showing how to navigate through each workflow and interact with the AI-powered tools.

**Duration**: 15-20 minutes  
**Audience**: Stakeholders, clients, or technical reviewers

---

## 📋 Pre-Demo Setup

### 1. Start the Application
```bash
cd legal-tech-assistant
python app.py
```
**Expected Output**: `Running on http://127.0.0.1:5000`

### 2. Open Browser
Navigate to: `http://localhost:5000`

---

## 🚀 Demo Flow

### **Phase 1: Authentication & Setup (2 minutes)**

#### Step 1: Login
1. **Click**: "Login" button
2. **Enter Email**: `sarah.johnson@bbg.com` (Legal Team - Full Access)
3. **Click**: "Login" button
4. **Expected**: Welcome message and redirect to category selection

#### Step 2: Select Product Category
1. **Click**: "Wine" category card
2. **Click**: "Select Category" button
3. **Expected**: Redirect to main dashboard

---

### **Phase 2: Dashboard Overview (1 minute)**

#### Step 3: Explore Dashboard
**Say**: "This is the main dashboard showing all available workflows based on user permissions."

**Point out**:
- Product category badge (Wine) in top-right
- User profile with role (Legal)
- Workflow cards with status indicators
- Navigation sidebar

**Click**: "View All Workflows" to show the full workflow grid

---

### **Phase 3: Agreement Replication Workflow (4 minutes)**

#### Step 4: Start Agreement Replication
1. **Click**: "Agreement Replication" card
2. **Say**: "This workflow allows us to take an existing agreement and replicate it for different states with AI-powered compliance modifications."

#### Step 5: Upload Agreement
1. **Click**: "Choose File" button
2. **Select**: Any sample document (or create a text file with "Sample Distribution Agreement")
3. **Expected**: File name appears in the upload area

#### Step 6: Configure Replication
1. **Select Original State**: "California" from dropdown
2. **Select Target States**: 
   - Check "New York"
   - Check "Texas" 
   - Check "Florida"
3. **Click**: "Replicate Agreement" button

#### Step 7: Review Results
**Say**: "The AI has analyzed the agreement and generated state-specific modifications."

**Point out**:
- Processing status for each state
- State-specific modifications listed
- Download links for each replicated agreement
- Professional results presentation

**Click**: "Download" for one of the states to show the generated agreement

---

### **Phase 4: Create New Agreement Workflow (4 minutes)**

#### Step 8: Start Create Agreement
1. **Navigate back** to dashboard
2. **Click**: "Create New Agreement" card
3. **Say**: "This is a comprehensive wizard for creating new distribution agreements with AI-powered recommendations."

#### Step 9: Basic Information (Step 0)
1. **Agreement Type**: Select "Distribution Agreement" from dropdown
2. **Target State**: Select "California" from dropdown
3. **Agreement Title**: Type "Premium Wine Distribution Agreement - California"
4. **Click**: "Next" button

#### Step 10: Parties Information (Step 1)
1. **Supplier Name**: "Premium Wines Inc."
2. **Distributor Name**: "California Distribution Co."
3. **Effective Date**: Select today's date
4. **Click**: "Next" button

#### Step 11: Terms & Conditions (Step 2)
1. **Territory**: "California, Nevada, Arizona"
2. **Term Length**: "5 years"
3. **Minimum Purchase**: "$500,000 annually"
4. **Click**: "Next" button

#### Step 12: AI-Powered Recommendations (Step 3)
**Say**: "The AI analyzes the entered information and provides intelligent recommendations."

**Point out**:
- Modern card-based recommendation layout
- Color-coded recommendation types
- Specific suggestions for improvement
- Professional presentation

**Click**: "Next" button

#### Step 13: Generate Agreement (Step 4)
1. **Click**: "Generate Agreement" button
2. **Say**: "The system generates a complete agreement based on the provided information and AI recommendations."
3. **Click**: "Download Agreement" to show the generated document

---

### **Phase 5: Contract Q&A Workflow (3 minutes)**

#### Step 14: Start Contract Q&A
1. **Navigate back** to dashboard
2. **Click**: "Contract Q&A" card
3. **Say**: "This is an interactive AI assistant for analyzing uploaded contracts and answering questions."

#### Step 15: Select Contract
1. **Contract Dropdown**: Select "Sample Distribution Agreement - Supplier X"
2. **Say**: "We can select from previously uploaded contracts for analysis."

#### Step 16: Ask Questions
1. **Type**: "What are the termination requirements?"
2. **Press**: Enter or click "Send"
3. **Wait**: 2 seconds for "thinking" animation
4. **Point out**: AI response with source citations

#### Step 17: Interactive Features
1. **Hover over**: Source citation to show tooltip
2. **Click**: Source citation to demonstrate download functionality
3. **Type**: "What are the payment terms?"
4. **Press**: Enter
5. **Point out**: Usage statistics updating in real-time

#### Step 18: Filter Usage Stats
1. **Click**: "Week" filter
2. **Click**: "Day" filter (shows 0/0 for session-based)
3. **Click**: "Month" filter (shows realistic numbers)

---

### **Phase 6: Financial Analysis Workflow (3 minutes)**

#### Step 19: Start Financial Analysis
1. **Navigate back** to dashboard
2. **Click**: "Financial Analysis" card
3. **Say**: "This workflow provides comprehensive financial analysis of contract obligations and payment terms."

#### Step 20: Review Financial Dashboard
**Point out**:
- Dark mode interface consistency
- Financial metrics and charts
- Contract analysis details table
- Risk alerts (permanent, not disappearing)

#### Step 21: Interact with Analysis
1. **Hover over**: Different sections of the financial charts
2. **Point out**: Detailed contract analysis table
3. **Click**: On different risk alert items
4. **Say**: "All risk alerts remain visible and don't auto-dismiss"

---

### **Phase 7: Knowledge Base Workflow (2 minutes)**

#### Step 22: Start Knowledge Base
1. **Navigate back** to dashboard
2. **Click**: "Knowledge Base" card
3. **Say**: "This is the centralized repository for all legal documents, templates, and resources."

#### Step 23: Explore Knowledge Base
**Point out**:
- Dark mode interface
- Document categories and organization
- Search functionality
- Modern card-based layout
- Smooth sidebar animations

---

### **Phase 8: User Role Demonstration (2 minutes)**

#### Step 24: Switch to Finance User
1. **Click**: User profile in top-right
2. **Click**: "Logout"
3. **Enter Email**: `mike.chen@bbg.com` (Finance Team)
4. **Click**: "Login"
5. **Select**: "Spirit" category
6. **Click**: "Select Category"

#### Step 25: Show Role Restrictions
**Point out**:
- Limited workflow access (Financial Analysis, Contract Q&A, Knowledge Base)
- "Access Denied" message for restricted workflows
- Role-appropriate interface

#### Step 26: Test Finance Workflow
1. **Click**: "Financial Analysis"
2. **Say**: "Finance users have full access to financial analysis tools"
3. **Navigate back** to dashboard

---

### **Phase 9: Mobile Responsiveness (1 minute)**

#### Step 27: Mobile View
1. **Open**: Browser developer tools (F12)
2. **Click**: Mobile device toggle
3. **Select**: iPhone or Android view
4. **Say**: "The application is fully responsive and works on all devices"
5. **Navigate**: Through different pages to show mobile layout

---

## 🎯 Key Demo Points to Emphasize

### **Technical Excellence**
- **Dark Mode Consistency**: Every page maintains the professional dark theme
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Modern UI/UX**: Glassmorphism effects, smooth animations, professional styling
- **Role-Based Security**: Different access levels for different user types

### **AI-Powered Features**
- **Intelligent Recommendations**: AI suggests improvements and modifications
- **Natural Language Processing**: Chat interface understands complex legal questions
- **Source Citations**: Every AI response includes verifiable source references
- **State-Specific Compliance**: Automated legal requirement analysis

### **Workflow Efficiency**
- **Multi-Step Wizards**: Guided processes for complex tasks
- **Batch Processing**: Handle multiple states or documents simultaneously
- **Real-Time Validation**: Immediate feedback and error prevention
- **Export Capabilities**: Download generated documents and reports

### **User Experience**
- **Intuitive Navigation**: Clear workflow progression and status indicators
- **Interactive Elements**: Hover effects, tooltips, and dynamic content
- **Professional Presentation**: Clean, modern interface suitable for legal professionals
- **Comprehensive Analytics**: Usage statistics and performance metrics

---

## 🚨 Demo Troubleshooting

### **Common Issues & Solutions**

#### Issue: Dropdowns showing white background
**Solution**: The dropdowns are designed to work with the global CSS overrides. The white background with dark text is the intended behavior.

#### Issue: AI responses seem slow
**Solution**: The 2-second delay is intentional to show the "thinking" animation and simulate real AI processing time.

#### Issue: File upload not working
**Solution**: Use any text file or create a simple document. The system accepts any file type for demo purposes.

#### Issue: Navigation between steps not working
**Solution**: Ensure you're clicking the "Next" buttons and not using browser navigation during the wizard.

---

## 📝 Demo Script Notes

### **Timing Guidelines**
- **Total Duration**: 15-20 minutes
- **Allow Questions**: 5-10 minutes for Q&A
- **Buffer Time**: 5 minutes for technical issues

### **Audience Adaptation**
- **Technical Audience**: Focus on architecture, API endpoints, and code quality
- **Business Audience**: Emphasize workflow efficiency and ROI
- **Legal Audience**: Highlight compliance features and document accuracy

### **Follow-up Actions**
- **Technical Review**: Provide access to code repository
- **Business Review**: Schedule follow-up meeting for requirements discussion
- **Legal Review**: Arrange demo with legal team for compliance validation

---

## 🎉 Demo Conclusion

**Closing Statement**: "The Legal Tech Assistant represents a comprehensive solution for modern legal workflows, combining AI-powered intelligence with intuitive user experience to streamline beverage distribution agreement management. The system is designed to scale with your organization's needs while maintaining the highest standards of security and compliance."

**Next Steps**:
1. Technical evaluation and feedback
2. Integration planning and timeline
3. User training and onboarding
4. Production deployment strategy

---

*This demo script ensures a comprehensive showcase of all Legal Tech Assistant features while maintaining professional presentation standards.*
